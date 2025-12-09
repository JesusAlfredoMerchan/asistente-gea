import { Suggestion } from '../types'
import './Suggestions.css'

interface SuggestionsProps {
  suggestions: Suggestion[]
  onSuggestionClick: (suggestion: Suggestion) => void
}

const Suggestions = ({ suggestions, onSuggestionClick }: SuggestionsProps) => {
  return (
    <div className="suggestions-container">
      <div className="suggestions-label">Preguntas sugeridas:</div>
      <div className="suggestions-list">
        {suggestions.map((suggestion) => (
          <button
            key={suggestion.id}
            className="suggestion-button"
            onClick={() => onSuggestionClick(suggestion)}
          >
            {suggestion.text}
          </button>
        ))}
      </div>
    </div>
  )
}

export default Suggestions

