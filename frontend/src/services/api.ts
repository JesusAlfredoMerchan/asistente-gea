import axios from 'axios'

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

// Log para debugging (solo en desarrollo)
if (import.meta.env.DEV) {
  console.log('🔧 API Base URL:', API_BASE_URL)
  console.log('🔧 VITE_API_URL env var:', import.meta.env.VITE_API_URL)
}

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 10000, // 10 segundos de timeout para evitar que se quede colgado
})

// Interceptor para manejar errores globalmente
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.code === 'ERR_NETWORK' || error.message.includes('Network Error')) {
      console.error('❌ Error de conexión con el backend:', {
        url: API_BASE_URL,
        error: error.message,
        hint: 'Verifica que VITE_API_URL esté configurada en Vercel'
      })
    }
    return Promise.reject(error)
  }
)

export interface ChatResponse {
  response: string
  conversation_id: string
  suggestions?: string[]
}

export interface SuggestionsResponse {
  suggestions: string[]
}

export interface ModelStatus {
  current_model: string | null
  available_models: string[]
  models_quota_status: {
    [modelName: string]: {
      exceeded: boolean
      request_count: number
      remaining_time: {
        hours: number
        minutes: number
        total_seconds: number
      } | null
      is_current: boolean
    }
  }
}

export const sendMessage = async (
  message: string,
  conversationId: string | null
): Promise<ChatResponse> => {
  const response = await api.post<ChatResponse>('/api/chat', {
    message,
    conversation_id: conversationId,
  })
  return response.data
}

export const getSuggestions = async (): Promise<SuggestionsResponse> => {
  const response = await api.get<SuggestionsResponse>('/api/suggestions')
  return response.data
}

export const getModelStatus = async (): Promise<ModelStatus> => {
  const response = await api.get<ModelStatus>('/api/models')
  return response.data
}

export const changeModel = async (modelName: string): Promise<{ success: boolean; message: string; current_model?: string }> => {
  const response = await api.post<{ success: boolean; message: string; current_model?: string }>('/api/models/change', {
    model_name: modelName
  })
  return response.data
}

export const healthCheck = async (): Promise<{ status: string }> => {
  const response = await api.get('/api/health')
  return response.data
}

