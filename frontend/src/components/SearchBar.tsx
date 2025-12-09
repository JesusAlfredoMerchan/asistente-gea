import { useState, useEffect, useRef } from 'react'
import { Message } from '../types'
import './SearchBar.css'

interface SearchBarProps {
  messages: Message[]
  onSearchResults: (results: Message[]) => void
  onHighlightMessage: (messageId: string | null) => void
  onOpenChange?: (isOpen: boolean) => void
}

const SearchBar = ({ messages, onSearchResults, onHighlightMessage, onOpenChange }: SearchBarProps) => {
  const [searchQuery, setSearchQuery] = useState('')
  const [isOpen, setIsOpen] = useState(false)
  const [currentResultIndex, setCurrentResultIndex] = useState(-1)
  const searchInputRef = useRef<HTMLInputElement>(null)
  const searchButtonRef = useRef<HTMLButtonElement>(null)

  // Exponer función para abrir desde fuera
  useEffect(() => {
    if (onOpenChange) {
      onOpenChange(isOpen)
    }
  }, [isOpen, onOpenChange])

  // Exponer función para abrir búsqueda
  useEffect(() => {
    const handleOpenSearch = () => {
      setIsOpen(true)
      setTimeout(() => searchInputRef.current?.focus(), 100)
    }
    
    window.addEventListener('open-search', handleOpenSearch)
    return () => window.removeEventListener('open-search', handleOpenSearch)
  }, [])

  // El atajo Ctrl+K se maneja desde ChatInterface usando useKeyboardShortcuts
  // Solo manejamos Escape localmente cuando el search está abierto
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape' && isOpen) {
        setIsOpen(false)
        setSearchQuery('')
        onHighlightMessage(null)
      }
    }

    window.addEventListener('keydown', handleKeyDown)
    return () => window.removeEventListener('keydown', handleKeyDown)
  }, [isOpen, onHighlightMessage])

  // Buscar mensajes cuando cambia la query
  useEffect(() => {
    if (!searchQuery.trim()) {
      onSearchResults([])
      onHighlightMessage(null)
      setCurrentResultIndex(-1)
      return
    }

    const query = searchQuery.toLowerCase()
    const results = messages.filter(msg => 
      msg.text.toLowerCase().includes(query)
    )

    onSearchResults(results)
    if (results.length > 0) {
      setCurrentResultIndex(0)
      onHighlightMessage(results[0].id)
    } else {
      setCurrentResultIndex(-1)
      onHighlightMessage(null)
    }
  }, [searchQuery, messages, onSearchResults, onHighlightMessage])

  const handleNext = () => {
    const query = searchQuery.toLowerCase()
    const results = messages.filter(msg => 
      msg.text.toLowerCase().includes(query)
    )
    
    if (results.length > 0) {
      const nextIndex = (currentResultIndex + 1) % results.length
      setCurrentResultIndex(nextIndex)
      onHighlightMessage(results[nextIndex].id)
      
      // Scroll al mensaje
      const messageElement = document.querySelector(`[data-message-id="${results[nextIndex].id}"]`)
      messageElement?.scrollIntoView({ behavior: 'smooth', block: 'center' })
    }
  }

  const handlePrevious = () => {
    const query = searchQuery.toLowerCase()
    const results = messages.filter(msg => 
      msg.text.toLowerCase().includes(query)
    )
    
    if (results.length > 0) {
      const prevIndex = currentResultIndex <= 0 ? results.length - 1 : currentResultIndex - 1
      setCurrentResultIndex(prevIndex)
      onHighlightMessage(results[prevIndex].id)
      
      // Scroll al mensaje
      const messageElement = document.querySelector(`[data-message-id="${results[prevIndex].id}"]`)
      messageElement?.scrollIntoView({ behavior: 'smooth', block: 'center' })
    }
  }

  if (!isOpen) {
    return (
      <button
        ref={searchButtonRef}
        className="search-toggle-btn"
        onClick={() => {
          setIsOpen(true)
          setTimeout(() => searchInputRef.current?.focus(), 100)
        }}
        title="Buscar en conversación (Ctrl/Cmd + K)"
      >
        🔍
      </button>
    )
  }

  const query = searchQuery.toLowerCase()
  const results = messages.filter(msg => 
    msg.text.toLowerCase().includes(query)
  )

  return (
    <div className="search-bar-container">
      <div className="search-bar">
        <span className="search-icon">🔍</span>
        <input
          ref={searchInputRef}
          type="text"
          className="search-input"
          placeholder="Buscar en conversación..."
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === 'Enter' && e.shiftKey) {
              handlePrevious()
            } else if (e.key === 'Enter') {
              handleNext()
            }
          }}
        />
        {searchQuery && (
          <div className="search-results-count">
            {currentResultIndex + 1} / {results.length}
          </div>
        )}
        <div className="search-actions">
          {searchQuery && results.length > 0 && (
            <>
              <button
                className="search-nav-btn"
                onClick={handlePrevious}
                title="Anterior (Shift + Enter)"
              >
                ↑
              </button>
              <button
                className="search-nav-btn"
                onClick={handleNext}
                title="Siguiente (Enter)"
              >
                ↓
              </button>
            </>
          )}
          <button
            className="search-close-btn"
            onClick={() => {
              setIsOpen(false)
              setSearchQuery('')
              onHighlightMessage(null)
            }}
            title="Cerrar (Esc)"
          >
            ✕
          </button>
        </div>
      </div>
      {searchQuery && results.length === 0 && (
        <div className="search-no-results">No se encontraron resultados</div>
      )}
    </div>
  )
}

export default SearchBar

