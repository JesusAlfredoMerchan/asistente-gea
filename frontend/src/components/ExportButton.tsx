import { useState } from 'react'
import { Message } from '../types'
import { useToast } from '../hooks/useToast'
import './ExportButton.css'

interface ExportButtonProps {
  messages: Message[]
}

const ExportButton = ({ messages }: ExportButtonProps) => {
  const { showToast } = useToast()

  const exportToTXT = () => {
    const content = messages.map(msg => {
      const date = msg.timestamp.toLocaleString('es-ES')
      const sender = msg.sender === 'user' ? 'Usuario' : 'Asistente'
      return `[${date}] ${sender}:\n${msg.text}\n\n`
    }).join('---\n\n')

    const blob = new Blob([content], { type: 'text/plain;charset=utf-8' })
    const url = URL.createObjectURL(blob)
    const link = document.createElement('a')
    link.href = url
    link.download = `conversacion-gea-${new Date().toISOString().split('T')[0]}.txt`
    link.click()
    URL.revokeObjectURL(url)
    showToast('Conversación exportada como TXT', 'success')
  }

  const exportToMarkdown = () => {
    const content = `# Conversación GEA\n\n*Exportada el ${new Date().toLocaleString('es-ES')}*\n\n---\n\n` +
      messages.map(msg => {
        const date = msg.timestamp.toLocaleString('es-ES')
        const sender = msg.sender === 'user' ? '**Usuario**' : '**Asistente**'
        return `## ${sender}\n\n*${date}*\n\n${msg.text}\n\n---\n\n`
      }).join('')

    const blob = new Blob([content], { type: 'text/markdown;charset=utf-8' })
    const url = URL.createObjectURL(blob)
    const link = document.createElement('a')
    link.href = url
    link.download = `conversacion-gea-${new Date().toISOString().split('T')[0]}.md`
    link.click()
    URL.revokeObjectURL(url)
    showToast('Conversación exportada como Markdown', 'success')
  }

  const exportToJSON = () => {
    const data = {
      exportDate: new Date().toISOString(),
      totalMessages: messages.length,
      messages: messages.map(msg => ({
        id: msg.id,
        text: msg.text,
        sender: msg.sender,
        timestamp: msg.timestamp.toISOString()
      }))
    }

    const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json;charset=utf-8' })
    const url = URL.createObjectURL(blob)
    const link = document.createElement('a')
    link.href = url
    link.download = `conversacion-gea-${new Date().toISOString().split('T')[0]}.json`
    link.click()
    URL.revokeObjectURL(url)
    showToast('Conversación exportada como JSON', 'success')
  }

  const [showMenu, setShowMenu] = useState(false)

  if (messages.length <= 1) {
    return null // No mostrar si solo hay mensaje de bienvenida
  }

  return (
    <div className="export-button-container">
      <button
        className="export-button"
        onClick={() => setShowMenu(!showMenu)}
        title="Exportar conversación"
      >
        📥
      </button>
      {showMenu && (
        <div className="export-menu">
          <button
            className="export-option"
            onClick={() => {
              exportToTXT()
              setShowMenu(false)
            }}
          >
            📄 Exportar como TXT
          </button>
          <button
            className="export-option"
            onClick={() => {
              exportToMarkdown()
              setShowMenu(false)
            }}
          >
            📝 Exportar como Markdown
          </button>
          <button
            className="export-option"
            onClick={() => {
              exportToJSON()
              setShowMenu(false)
            }}
          >
            📊 Exportar como JSON
          </button>
        </div>
      )}
      {showMenu && (
        <div
          className="export-menu-overlay"
          onClick={() => setShowMenu(false)}
        />
      )}
    </div>
  )
}

export default ExportButton

