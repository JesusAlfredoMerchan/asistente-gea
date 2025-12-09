import { useEffect, useRef } from 'react'

interface KeyboardShortcuts {
  onEnter?: () => void
  onCtrlK?: () => void
  onCtrlL?: () => void
  onEscape?: () => void
  enabled?: boolean
}

export const useKeyboardShortcuts = ({
  onEnter,
  onCtrlK,
  onCtrlL,
  onEscape,
  enabled = true
}: KeyboardShortcuts) => {
  const callbacksRef = useRef({ onEnter, onCtrlK, onCtrlL, onEscape })

  useEffect(() => {
    callbacksRef.current = { onEnter, onCtrlK, onCtrlL, onEscape }
  }, [onEnter, onCtrlK, onCtrlL, onEscape])

  useEffect(() => {
    if (!enabled) return

    const handleKeyDown = (e: KeyboardEvent) => {
      // Ignorar si está escribiendo en un input o textarea
      const target = e.target as HTMLElement
      if (target.tagName === 'INPUT' || target.tagName === 'TEXTAREA') {
        // Permitir Ctrl+K y Ctrl+L incluso en inputs
        if (e.ctrlKey || e.metaKey) {
          if (e.key === 'k' && callbacksRef.current.onCtrlK) {
            e.preventDefault()
            callbacksRef.current.onCtrlK()
            return
          }
          if (e.key === 'l' && callbacksRef.current.onCtrlL) {
            e.preventDefault()
            callbacksRef.current.onCtrlL()
            return
          }
        }
        // Permitir Escape en cualquier lugar
        if (e.key === 'Escape' && callbacksRef.current.onEscape) {
          e.preventDefault()
          callbacksRef.current.onEscape()
          return
        }
        return
      }

      // Atajos globales
      if (e.ctrlKey || e.metaKey) {
        if (e.key === 'k' && callbacksRef.current.onCtrlK) {
          e.preventDefault()
          callbacksRef.current.onCtrlK()
        } else if (e.key === 'l' && callbacksRef.current.onCtrlL) {
          e.preventDefault()
          callbacksRef.current.onCtrlL()
        }
      }

      if (e.key === 'Escape' && callbacksRef.current.onEscape) {
        e.preventDefault()
        callbacksRef.current.onEscape()
      }
    }

    window.addEventListener('keydown', handleKeyDown)
    return () => window.removeEventListener('keydown', handleKeyDown)
  }, [enabled])
}

