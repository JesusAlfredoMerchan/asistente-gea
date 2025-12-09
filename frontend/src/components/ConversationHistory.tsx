import { useState, useEffect } from 'react'
import { Message } from '../types'
import './ConversationHistory.css'

interface Conversation {
  id: string
  name: string
  messages: Message[]
  conversationId: string | null
  lastUpdated: Date
}

interface ConversationHistoryProps {
  currentConversationId: string | null
  currentMessages: Message[]
  onSelectConversation: (conversation: Conversation) => void
  onNewConversation: () => void
  onDeleteConversation: (id: string) => void
}

const CONVERSATIONS_STORAGE_KEY = 'gea-conversations'

const ConversationHistory = ({
  currentConversationId,
  currentMessages,
  onSelectConversation,
  onNewConversation,
  onDeleteConversation
}: ConversationHistoryProps) => {
  const [conversations, setConversations] = useState<Conversation[]>([])
  const [isOpen, setIsOpen] = useState(false)
  const [editingId, setEditingId] = useState<string | null>(null)
  const [editName, setEditName] = useState('')

  // Cargar conversaciones al iniciar
  useEffect(() => {
    loadConversations()
  }, [])

  // Guardar conversación actual cuando cambien los mensajes
  useEffect(() => {
    if (currentMessages.length > 1) {
      saveCurrentConversation()
    }
  }, [currentMessages, currentConversationId])

  const loadConversations = () => {
    try {
      const saved = localStorage.getItem(CONVERSATIONS_STORAGE_KEY)
      if (saved) {
        const parsed = JSON.parse(saved).map((conv: any) => ({
          ...conv,
          lastUpdated: new Date(conv.lastUpdated),
          messages: conv.messages.map((msg: any) => ({
            ...msg,
            timestamp: new Date(msg.timestamp)
          }))
        }))
        setConversations(parsed.sort((a: Conversation, b: Conversation) => 
          b.lastUpdated.getTime() - a.lastUpdated.getTime()
        ))
      }
    } catch (error) {
      console.error('Error cargando conversaciones:', error)
    }
  }

  const saveCurrentConversation = () => {
    try {
      const existing = conversations.find(c => c.conversationId === currentConversationId)
      
      if (existing) {
        // Actualizar conversación existente
        const updated = conversations.map(c => 
          c.id === existing.id
            ? {
                ...c,
                messages: currentMessages,
                lastUpdated: new Date()
              }
            : c
        )
        setConversations(updated)
        localStorage.setItem(CONVERSATIONS_STORAGE_KEY, JSON.stringify(updated))
      } else if (currentConversationId) {
        // Crear nueva conversación
        const firstUserMessage = currentMessages.find(m => m.sender === 'user')
        const name = firstUserMessage 
          ? firstUserMessage.text.slice(0, 50) + (firstUserMessage.text.length > 50 ? '...' : '')
          : 'Nueva conversación'
        
        const newConv: Conversation = {
          id: `conv-${Date.now()}`,
          name,
          messages: currentMessages,
          conversationId: currentConversationId,
          lastUpdated: new Date()
        }
        
        const updated = [newConv, ...conversations]
        setConversations(updated)
        localStorage.setItem(CONVERSATIONS_STORAGE_KEY, JSON.stringify(updated))
      }
    } catch (error) {
      console.error('Error guardando conversación:', error)
    }
  }

  const handleSelect = (conversation: Conversation) => {
    onSelectConversation(conversation)
    setIsOpen(false)
  }

  const handleDelete = (id: string, e: React.MouseEvent) => {
    e.stopPropagation()
    const convToDelete = conversations.find(c => c.id === id)
    const isActive = convToDelete?.conversationId === currentConversationId
    
    const message = isActive
      ? '¿Estás seguro de que quieres eliminar esta conversación? El chat actual se limpiará.'
      : '¿Estás seguro de que quieres eliminar esta conversación?'
    
    if (window.confirm(message)) {
      onDeleteConversation(id)
      const updated = conversations.filter(c => c.id !== id)
      setConversations(updated)
      localStorage.setItem(CONVERSATIONS_STORAGE_KEY, JSON.stringify(updated))
    }
  }

  const handleEdit = (id: string, currentName: string, e: React.MouseEvent) => {
    e.stopPropagation()
    setEditingId(id)
    setEditName(currentName)
  }

  const handleSaveEdit = (id: string) => {
    const updated = conversations.map(c =>
      c.id === id ? { ...c, name: editName.trim() || 'Sin título' } : c
    )
    setConversations(updated)
    localStorage.setItem(CONVERSATIONS_STORAGE_KEY, JSON.stringify(updated))
    setEditingId(null)
    setEditName('')
  }

  const handleCancelEdit = () => {
    setEditingId(null)
    setEditName('')
  }

  return (
    <>
      <button
        className="conversation-history-toggle"
        onClick={() => setIsOpen(!isOpen)}
        title="Historial de conversaciones"
      >
        💬
      </button>
      
      {isOpen && (
        <>
          <div className="conversation-history-overlay" onClick={() => setIsOpen(false)} />
          <div className="conversation-history-panel">
            <div className="conversation-history-header">
              <h3>Conversaciones</h3>
              <button
                className="conversation-history-close"
                onClick={() => setIsOpen(false)}
                title="Cerrar"
              >
                ×
              </button>
            </div>
            
            <button
              className="new-conversation-btn"
              onClick={() => {
                onNewConversation()
                setIsOpen(false)
              }}
            >
              + Nueva conversación
            </button>

            <div className="conversations-list">
              {conversations.length === 0 ? (
                <div className="no-conversations">
                  No hay conversaciones guardadas
                </div>
              ) : (
                conversations.map(conv => (
                  <div
                    key={conv.id}
                    className={`conversation-item ${
                      conv.conversationId === currentConversationId ? 'active' : ''
                    }`}
                    onClick={() => handleSelect(conv)}
                  >
                    {editingId === conv.id ? (
                      <div className="conversation-edit" onClick={(e) => e.stopPropagation()}>
                        <input
                          type="text"
                          value={editName}
                          onChange={(e) => setEditName(e.target.value)}
                          onKeyDown={(e) => {
                            if (e.key === 'Enter') handleSaveEdit(conv.id)
                            if (e.key === 'Escape') handleCancelEdit()
                          }}
                          autoFocus
                          className="conversation-edit-input"
                        />
                        <button
                          className="conversation-edit-save"
                          onClick={() => handleSaveEdit(conv.id)}
                        >
                          ✓
                        </button>
                        <button
                          className="conversation-edit-cancel"
                          onClick={handleCancelEdit}
                        >
                          ✕
                        </button>
                      </div>
                    ) : (
                      <>
                        <div className="conversation-info">
                          <div className="conversation-name">{conv.name}</div>
                          <div className="conversation-meta">
                            {conv.messages.filter(m => m.sender === 'user').length} mensajes ·{' '}
                            {conv.lastUpdated.toLocaleDateString('es-ES', {
                              day: '2-digit',
                              month: '2-digit',
                              hour: '2-digit',
                              minute: '2-digit'
                            })}
                          </div>
                        </div>
                        <div className="conversation-actions">
                          <button
                            className="conversation-edit-btn"
                            onClick={(e) => handleEdit(conv.id, conv.name, e)}
                            title="Renombrar"
                          >
                            ✏️
                          </button>
                          <button
                            className="conversation-delete-btn"
                            onClick={(e) => handleDelete(conv.id, e)}
                            title="Eliminar"
                          >
                            🗑️
                          </button>
                        </div>
                      </>
                    )}
                  </div>
                ))
              )}
            </div>
          </div>
        </>
      )}
    </>
  )
}

export default ConversationHistory

