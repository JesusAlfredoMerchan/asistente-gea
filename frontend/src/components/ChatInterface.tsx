import { useState, useRef, useEffect } from 'react'
import MessageList from './MessageList'
import MessageInput from './MessageInput'
import Suggestions from './Suggestions'
import SearchBar from './SearchBar'
import ExportButton from './ExportButton'
import ConversationHistory from './ConversationHistory'
import { useToast } from '../hooks/useToast'
import { useKeyboardShortcuts } from '../hooks/useKeyboardShortcuts'
import { sendMessage, getSuggestions } from '../services/api'
import type { Message, Suggestion } from '../types'
import './ChatInterface.css'

const STORAGE_KEY = 'gea-chat-messages'
const CONVERSATION_KEY = 'gea-conversation-id'

const ChatInterface = () => {
  const [messages, setMessages] = useState<Message[]>([])
  const [suggestions, setSuggestions] = useState<Suggestion[]>([])
  const [isLoading, setIsLoading] = useState(false)
  const [conversationId, setConversationId] = useState<string | null>(null)
  const [highlightedMessageId, setHighlightedMessageId] = useState<string | null>(null)
  const [showClearConfirm, setShowClearConfirm] = useState(false)
  const [isSearchOpen, setIsSearchOpen] = useState(false)
  const messagesEndRef = useRef<HTMLDivElement>(null)
  const { showToast, ToastContainer } = useToast()

  // Cargar mensajes desde localStorage al iniciar
  useEffect(() => {
    const savedMessages = localStorage.getItem(STORAGE_KEY)
    const savedConversationId = localStorage.getItem(CONVERSATION_KEY)
    
    if (savedMessages) {
      try {
        const parsedMessages = JSON.parse(savedMessages).map((msg: any) => ({
          ...msg,
          timestamp: new Date(msg.timestamp)
        }))
        setMessages(parsedMessages)
      } catch (error) {
        console.error('Error cargando mensajes guardados:', error)
        // Si hay error, inicializar con mensaje de bienvenida
        initializeWelcomeMessage()
      }
    } else {
      initializeWelcomeMessage()
    }
    
    if (savedConversationId) {
      setConversationId(savedConversationId)
    }
    
    // Cargar sugerencias iniciales
    loadInitialSuggestions()
  }, [])

  // Guardar mensajes en localStorage cuando cambien
  useEffect(() => {
    if (messages.length > 0) {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(messages))
    }
  }, [messages])

  // Guardar conversationId en localStorage cuando cambie
  useEffect(() => {
    if (conversationId) {
      localStorage.setItem(CONVERSATION_KEY, conversationId)
    }
  }, [conversationId])

  const initializeWelcomeMessage = () => {
    setMessages([{
      id: 'welcome',
      text: '¡Hola! 👋 Soy tu asistente inteligente para GEA. Puedo ayudarte a entender y usar el sistema. ¿En qué puedo ayudarte?',
      sender: 'assistant',
      timestamp: new Date()
    }])
  }

  const clearConversation = (skipConfirmation = false) => {
    if (!skipConfirmation && !showClearConfirm) {
      setShowClearConfirm(true)
      return
    }

    // Limpiar estado
    setMessages([])
    setConversationId(null)
    setSuggestions([])
    
    // Limpiar localStorage
    localStorage.removeItem(STORAGE_KEY)
    localStorage.removeItem(CONVERSATION_KEY)
    
    // Reinicializar con mensaje de bienvenida
    initializeWelcomeMessage()
    loadInitialSuggestions()
    
    setShowClearConfirm(false)
    if (!skipConfirmation) {
      showToast('Conversación limpiada', 'success')
    }
  }

  const handleClearClick = () => {
    clearConversation()
  }

  const handleNewConversation = () => {
    clearConversation(true) // Saltar confirmación para nueva conversación
    showToast('Nueva conversación iniciada', 'info')
  }

  const handleSelectConversation = (conversation: any) => {
    setMessages(conversation.messages)
    setConversationId(conversation.conversationId)
    showToast(`Conversación "${conversation.name}" cargada`, 'success')
  }

  const handleDeleteConversation = (id: string) => {
    // Verificar si la conversación eliminada es la actual
    try {
      const saved = localStorage.getItem('gea-conversations')
      if (saved) {
        const conversations = JSON.parse(saved)
        const deletedConv = conversations.find((c: any) => c.id === id)
        
        // Si la conversación eliminada es la que está actualmente abierta
        if (deletedConv && deletedConv.conversationId === conversationId) {
          // Limpiar el chat actual
          setMessages([])
          setConversationId(null)
          setSuggestions([])
          localStorage.removeItem(STORAGE_KEY)
          localStorage.removeItem(CONVERSATION_KEY)
          initializeWelcomeMessage()
          loadInitialSuggestions()
          showToast('Conversación eliminada y chat limpiado', 'info')
        } else {
          showToast('Conversación eliminada', 'info')
        }
      }
    } catch (error) {
      console.error('Error verificando conversación eliminada:', error)
      showToast('Conversación eliminada', 'info')
    }
  }

  // Atajos de teclado
  useKeyboardShortcuts({
    onCtrlK: () => {
      // Abrir búsqueda
      if (!isSearchOpen) {
        window.dispatchEvent(new CustomEvent('open-search'))
      }
    },
    onCtrlL: () => {
      // Limpiar conversación
      if (!showClearConfirm) {
        clearConversation()
      }
    },
    onEscape: () => {
      // Cerrar confirmación si está abierta
      if (showClearConfirm) {
        setShowClearConfirm(false)
      }
    },
    enabled: !isSearchOpen // Deshabilitar atajos cuando el search está abierto
  })

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  const loadInitialSuggestions = async () => {
    try {
      const data = await getSuggestions()
      setSuggestions(data.suggestions.map((text, idx) => ({
        id: `suggestion-${idx}`,
        text
      })))
    } catch (error) {
      console.error('Error cargando sugerencias:', error)
    }
  }

  // Función para actualizar estado del modelo (puede ser llamada desde fuera)
  const updateModelStatus = async () => {
    // Disparar evento personalizado para que ModelStatus se actualice
    window.dispatchEvent(new CustomEvent('model-status-update'))
  }

  const handleSendMessage = async (text: string) => {
    if (!text.trim() || isLoading) return

    // Agregar mensaje del usuario
    const userMessage: Message = {
      id: `user-${Date.now()}`,
      text: text.trim(),
      sender: 'user',
      timestamp: new Date()
    }
    setMessages(prev => [...prev, userMessage])
    setIsLoading(true)

    try {
      const response = await sendMessage(text, conversationId)
      
      // Actualizar conversation ID si es nuevo
      if (response.conversation_id && !conversationId) {
        setConversationId(response.conversation_id)
      }

      // Agregar respuesta del asistente
      const assistantMessage: Message = {
        id: `assistant-${Date.now()}`,
        text: response.response,
        sender: 'assistant',
        timestamp: new Date()
      }
      setMessages(prev => [...prev, assistantMessage])

      // Actualizar sugerencias si vienen en la respuesta
      if (response.suggestions && response.suggestions.length > 0) {
        setSuggestions(response.suggestions.map((text, idx) => ({
          id: `suggestion-${Date.now()}-${idx}`,
          text
        })))
      }
      
      // Actualizar estado del modelo después de enviar mensaje
      updateModelStatus()
    } catch (error) {
      console.error('Error enviando mensaje:', error)
      const errorMessage: Message = {
        id: `error-${Date.now()}`,
        text: 'Lo siento, hubo un error al procesar tu mensaje. Por favor, intenta de nuevo.',
        sender: 'assistant',
        timestamp: new Date()
      }
      setMessages(prev => [...prev, errorMessage])
      showToast('Error al enviar mensaje', 'error')
    } finally {
      setIsLoading(false)
    }
  }

  const handleSuggestionClick = (suggestion: Suggestion) => {
    handleSendMessage(suggestion.text)
  }

  return (
    <div className="chat-interface">
      <ToastContainer />
      {messages.length > 1 && (
        <div className="chat-header-actions">
          <ConversationHistory
            currentConversationId={conversationId}
            currentMessages={messages}
            onSelectConversation={handleSelectConversation}
            onNewConversation={handleNewConversation}
            onDeleteConversation={handleDeleteConversation}
          />
          <SearchBar
            messages={messages}
            onSearchResults={() => {
              // Los resultados de búsqueda se manejan internamente en SearchBar
            }}
            onHighlightMessage={setHighlightedMessageId}
            onOpenChange={setIsSearchOpen}
          />
          <ExportButton messages={messages} />
          <button 
            className={`clear-conversation-btn ${showClearConfirm ? 'confirm' : ''}`}
            onClick={handleClearClick}
            title={showClearConfirm ? "Confirmar limpieza (Ctrl/Cmd + L)" : "Limpiar conversación (Ctrl/Cmd + L)"}
          >
            {showClearConfirm ? '✓ Confirmar' : '🗑️'}
          </button>
        </div>
      )}
      <div className="chat-messages-container">
        <MessageList 
          messages={messages} 
          isLoading={isLoading}
          highlightedMessageId={highlightedMessageId}
        />
        <div ref={messagesEndRef} />
      </div>
      
      {suggestions.length > 0 && messages.length <= 1 && (
        <Suggestions 
          suggestions={suggestions} 
          onSuggestionClick={handleSuggestionClick}
        />
      )}
      
      <MessageInput 
        onSendMessage={handleSendMessage}
        isLoading={isLoading}
      />
    </div>
  )
}

export default ChatInterface

