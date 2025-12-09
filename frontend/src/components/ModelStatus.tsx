import { useState, useEffect } from 'react'
import { getModelStatus, changeModel, type ModelStatus } from '../services/api'
import './ModelStatus.css'

const ModelStatusComponent = () => {
  const [status, setStatus] = useState<ModelStatus | null>(null)
  const [showAdvanced, setShowAdvanced] = useState(false)
  const [isChanging, setIsChanging] = useState(false)

  useEffect(() => {
    loadStatus()
    // Actualizar estado cada 30 segundos
    const interval = setInterval(loadStatus, 30000)
    
    // Escuchar eventos de actualización
    const handleUpdate = () => {
      loadStatus()
    }
    window.addEventListener('model-status-update', handleUpdate)
    
    return () => {
      clearInterval(interval)
      window.removeEventListener('model-status-update', handleUpdate)
    }
  }, [])

  const loadStatus = async () => {
    try {
      const data = await getModelStatus()
      setStatus(data)
    } catch (error) {
      console.error('Error cargando estado del modelo:', error)
    }
  }

  const handleModelChange = async (modelName: string) => {
    if (modelName === status?.current_model) return
    
    setIsChanging(true)
    try {
      const result = await changeModel(modelName)
      if (result.success) {
        await loadStatus()
        alert(result.message)
      } else {
        alert(`Error: ${result.message}`)
      }
    } catch (error) {
      console.error('Error cambiando modelo:', error)
      alert('Error al cambiar el modelo')
    } finally {
      setIsChanging(false)
    }
  }

  if (!status || !status.current_model) {
    return null
  }

  // Limpiar prefijo "models/" del nombre del modelo
  const cleanModelName = (name: string) => {
    let cleaned = name.replace('models/', '')
    
    // Si es OpenAI, mostrar nombre más claro
    if (cleaned.startsWith('openai:')) {
      return cleaned.replace('openai:', 'OpenAI ').replace(/gpt-(\d+\.\d+)/, 'GPT-$1').replace(/-/g, ' ')
    }
    
    // Para Gemini, limpiar prefijos
    cleaned = cleaned.replace(/^gemini-?/, '')
    
    // Convertir guiones a espacios y capitalizar
    cleaned = cleaned.replace(/-/g, ' ')
    
    return cleaned
  }

  const currentModelStatus = status.models_quota_status[status.current_model]
  const requestCount = currentModelStatus?.request_count || 0
  const isExceeded = currentModelStatus?.exceeded || false

  // Estimar límite (típicamente 20 para modelos flash, 15 para pro)
  const estimatedLimit = status.current_model.includes('flash') ? 20 : 15

  return (
    <div className="model-status-container">
      <div className="model-status-info">
        <span className="model-label">Modelo:</span>
        <span className="model-name">{cleanModelName(status.current_model)}</span>
        <span className="model-usage">
          {requestCount}/{estimatedLimit} requests
        </span>
        {isExceeded && (
          <span className="quota-warning" title="Cuota excedida para este modelo">
            ⚠️
          </span>
        )}
        <button 
          className="advanced-toggle"
          onClick={() => setShowAdvanced(!showAdvanced)}
          title="Configuración avanzada"
        >
          ⚙️
        </button>
      </div>

      {showAdvanced && (
        <div className="advanced-settings">
          <h3>Configuración Avanzada</h3>
          <div className="models-list">
            <p>Modelos disponibles ({status.available_models.length}):</p>
            {status.available_models.map((modelName) => {
              const modelStatus = status.models_quota_status[modelName]
              const isCurrent = modelName === status.current_model
              const isModelExceeded = modelStatus?.exceeded || false
              const modelRequestCount = modelStatus?.request_count || 0

              return (
                <div 
                  key={modelName} 
                  className={`model-option ${isCurrent ? 'current' : ''} ${isModelExceeded ? 'exceeded' : ''}`}
                >
                  <div className="model-option-info">
                    <span className="model-option-name">{cleanModelName(modelName)}</span>
                    <span className="model-option-usage">
                      {modelRequestCount} requests
                      {isModelExceeded && <span className="exceeded-badge">Excedido</span>}
                      {isCurrent && <span className="current-badge">Actual</span>}
                    </span>
                  </div>
                  {!isCurrent && !isChanging && (
                    <button 
                      onClick={() => handleModelChange(modelName)}
                      disabled={isModelExceeded}
                      className="change-model-btn"
                    >
                      Usar
                    </button>
                  )}
                </div>
              )
            })}
          </div>
          <p className="info-text">
            💡 El sistema cambia automáticamente entre modelos cuando se agota la cuota.
          </p>
        </div>
      )}
    </div>
  )
}

export default ModelStatusComponent

