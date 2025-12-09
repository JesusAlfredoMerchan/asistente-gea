import { useState, useEffect } from 'react'
import ChatInterface from './components/ChatInterface'
import ModelStatusComponent from './components/ModelStatus'
import ThemeToggle from './components/ThemeToggle'
import './App.css'

function App() {
  const [logoError, setLogoError] = useState(false)
  const logoPath = '/images/logos/Logo GEA.png'

  // Prevenir scroll automático al cargar
  useEffect(() => {
    window.scrollTo(0, 0)
    document.documentElement.scrollTop = 0
    document.body.scrollTop = 0
  }, [])

  // Forzar actualización del favicon
  useEffect(() => {
    const link = document.querySelector("link[rel~='icon']") as HTMLLinkElement
    if (link) {
      link.href = '/favicon.ico?' + new Date().getTime()
    } else {
      const newLink = document.createElement('link')
      newLink.rel = 'icon'
      newLink.type = 'image/x-icon'
      newLink.href = '/favicon.ico?' + new Date().getTime()
      document.head.appendChild(newLink)
    }
  }, [])

  return (
    <div className="app">
      <div className="app-container">
        <header className="app-header">
          <div className="header-content">
            {!logoError && (
              <div className="logo-container">
                <a 
                  href="http://www.improtecsa.com" 
                  target="_blank" 
                  rel="noopener noreferrer"
                  title="Visitar IMPROTECSA"
                >
                  <img 
                    src={logoPath} 
                    alt="Logo GEA - IMPROTECSA" 
                    className="gea-logo"
                    onLoad={() => {
                      console.log('Logo cargado exitosamente desde:', logoPath)
                    }}
                    onError={(e) => {
                      console.error('Error cargando logo desde:', logoPath)
                      console.error('Ruta completa esperada: frontend/public' + logoPath)
                      setLogoError(true)
                      e.currentTarget.style.display = 'none'
                    }}
                  />
                </a>
              </div>
            )}
            <div className="header-text">
              <h1>🤖 Asistente GEA</h1>
              <p>Sistema de Gestión Inteligente</p>
            </div>
            <div className="header-actions">
              <ThemeToggle />
              <div className="header-model-status">
                <ModelStatusComponent />
              </div>
            </div>
          </div>
        </header>
        <ChatInterface />
      </div>
    </div>
  )
}

export default App

