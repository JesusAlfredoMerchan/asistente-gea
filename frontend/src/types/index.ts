export interface Message {
  id: string
  text: string
  sender: 'user' | 'assistant'
  timestamp: Date
}

export interface Suggestion {
  id: string
  text: string
}

