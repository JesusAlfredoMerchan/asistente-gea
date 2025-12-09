import { useState, KeyboardEvent, useRef } from 'react'
import './MessageInput.css'

interface MessageInputProps {
  onSendMessage: (message: string) => void
  isLoading: boolean
}

const MessageInput = ({ onSendMessage, isLoading }: MessageInputProps) => {
  const [message, setMessage] = useState('')
  const inputRef = useRef<HTMLTextAreaElement>(null)

  const handleSend = () => {
    if (message.trim() && !isLoading) {
      // Efecto visual al enviar
      if (inputRef.current) {
        inputRef.current.classList.add('sending')
        setTimeout(() => {
          inputRef.current?.classList.remove('sending')
        }, 300)
      }
      
      onSendMessage(message)
      setMessage('')
    }
  }

  const handleKeyPress = (e: KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      handleSend()
    }
  }

  return (
    <div className="message-input-container">
      <div className="message-input-wrapper">
        <textarea
          ref={inputRef}
          className="message-input"
          placeholder="Escribe tu pregunta sobre GEA..."
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={handleKeyPress}
          rows={1}
          disabled={isLoading}
        />
        <button
          className="send-button"
          onClick={handleSend}
          disabled={!message.trim() || isLoading}
          aria-label="Enviar mensaje"
        >
          <svg
            width="20"
            height="20"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
          >
            <line x1="22" y1="2" x2="11" y2="13"></line>
            <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
          </svg>
        </button>
      </div>
    </div>
  )
}

export default MessageInput

