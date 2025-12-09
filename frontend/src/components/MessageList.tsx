import { Message } from '../types'
import MessageBubble from './MessageBubble'
import './MessageList.css'

interface MessageListProps {
  messages: Message[]
  isLoading: boolean
  highlightedMessageId?: string | null
}

const MessageList = ({ messages, isLoading, highlightedMessageId }: MessageListProps) => {
  return (
    <div className="message-list">
      {messages.map((message) => (
        <div
          key={message.id}
          data-message-id={message.id}
          className={highlightedMessageId === message.id ? 'highlighted-message' : ''}
        >
          <MessageBubble message={message} />
        </div>
      ))}
      {isLoading && (
        <div className="message-bubble assistant loading">
          <div className="typing-indicator">
            <span></span>
            <span></span>
            <span></span>
          </div>
        </div>
      )}
    </div>
  )
}

export default MessageList

