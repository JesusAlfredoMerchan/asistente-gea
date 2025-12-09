import { useState } from 'react'
import ReactMarkdown from 'react-markdown'
import { Message } from '../types'
import { useToast } from '../hooks/useToast'
import './MessageBubble.css'

interface MessageBubbleProps {
  message: Message
}

const MessageBubble = ({ message }: MessageBubbleProps) => {
  const [copied, setCopied] = useState(false)
  const { showToast } = useToast()

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(message.text)
      setCopied(true)
      showToast('Mensaje copiado al portapapeles', 'success')
      setTimeout(() => setCopied(false), 2000)
    } catch (error) {
      console.error('Error copiando al portapapeles:', error)
      // Fallback para navegadores antiguos
      const textArea = document.createElement('textarea')
      textArea.value = message.text
      document.body.appendChild(textArea)
      textArea.select()
      document.execCommand('copy')
      document.body.removeChild(textArea)
      setCopied(true)
      showToast('Mensaje copiado al portapapeles', 'success')
      setTimeout(() => setCopied(false), 2000)
    }
  }

  return (
    <div className={`message-bubble ${message.sender}`}>
      <div className="message-content">
        <ReactMarkdown
          components={{
            p: ({ children }) => <p>{children}</p>,
            strong: ({ children }) => <strong>{children}</strong>,
            em: ({ children }) => <em>{children}</em>,
            ul: ({ children }) => <ul>{children}</ul>,
            ol: ({ children }) => <ol>{children}</ol>,
            li: ({ children }) => <li>{children}</li>,
            code: ({ inline, children }) => 
              inline ? <code className="inline-code">{children}</code> : <code className="code-block">{children}</code>,
            blockquote: ({ children }) => <blockquote>{children}</blockquote>,
            a: ({ href, children }) => <a href={href} target="_blank" rel="noopener noreferrer">{children}</a>,
          }}
        >
          {message.text}
        </ReactMarkdown>
      </div>
      <div className="message-footer">
        <div className="message-time">
          {message.timestamp.toLocaleTimeString('es-ES', { 
            hour: '2-digit', 
            minute: '2-digit' 
          })}
        </div>
        {message.sender === 'assistant' && (
          <button
            className={`copy-button ${copied ? 'copied' : ''}`}
            onClick={handleCopy}
            title={copied ? '¡Copiado!' : 'Copiar respuesta'}
          >
            {copied ? '✓' : '📋'}
          </button>
        )}
      </div>
    </div>
  )
}

export default MessageBubble

