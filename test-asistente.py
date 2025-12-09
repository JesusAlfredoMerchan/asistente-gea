"""
Script de prueba para el Asistente GEA
Prueba diferentes tipos de preguntas para verificar el manejo de errores
"""
import requests
import json
import sys
import io

# Configurar salida UTF-8 para Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

API_URL = "http://localhost:8000/api/chat"

def test_question(question: str, description: str):
    """Probar una pregunta y mostrar el resultado"""
    print(f"\n{'='*60}")
    print(f"PRUEBA: {description}")
    print(f"Pregunta: {question}")
    print(f"{'='*60}")
    
    try:
        response = requests.post(
            API_URL,
            json={"message": question},
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"\n[OK] Respuesta recibida:")
            print(f"\n{data['response']}")
            
            if data.get('suggestions'):
                print(f"\n[SUGERENCIAS]:")
                for suggestion in data['suggestions']:
                    print(f"   - {suggestion}")
        else:
            print(f"\n[ERROR] {response.status_code}")
            try:
                print(response.text)
            except:
                print("No se pudo mostrar el error")
            
    except Exception as e:
        print(f"\n[ERROR] Error al conectar: {e}")

def main():
    print("\n" + "="*60)
    print("PRUEBAS DEL ASISTENTE GEA - Manejo de Errores")
    print("="*60)
    
    # Verificar que el servidor esté funcionando
    try:
        health = requests.get("http://localhost:8000/api/health", timeout=5)
        if health.status_code == 200:
            print("\n[OK] Servidor backend esta funcionando")
        else:
            print("\n[ERROR] Servidor backend no responde correctamente")
            return
    except Exception as e:
        print(f"\n[ERROR] No se puede conectar al servidor: {e}")
        print("   Asegurate de que el backend este ejecutandose en http://localhost:8000")
        return
    
    # Preguntas de prueba
    test_cases = [
        # Preguntas que SÍ deberían estar en la base de conocimiento
        ("¿Cómo creo un nuevo usuario?", "Pregunta válida sobre GEA"),
        ("¿Qué son las tareas pendientes?", "Pregunta válida sobre módulos"),
        ("¿Cómo asigno permisos a un perfil?", "Pregunta válida sobre procedimientos"),
        
        # Preguntas que NO deberían estar en la base de conocimiento
        ("¿Cómo cocino una pizza?", "Pregunta fuera del contexto de GEA"),
        ("¿Cuál es la capital de Francia?", "Pregunta general no relacionada"),
        ("¿Cómo instalo Windows 11?", "Pregunta técnica no relacionada con GEA"),
        ("¿Qué es la inteligencia artificial?", "Pregunta conceptual no relacionada"),
        
        # Preguntas sobre GEA pero que pueden no estar en la base de conocimiento
        ("¿Cómo exporto datos a Excel?", "Pregunta específica que puede no estar documentada"),
        ("¿Cuál es el límite de usuarios en GEA?", "Pregunta técnica específica"),
    ]
    
    print(f"\n[INFO] Ejecutando {len(test_cases)} pruebas...")
    
    for i, (question, description) in enumerate(test_cases, 1):
        test_question(question, description)
        if i < len(test_cases):
            print("\n" + "-"*60)
            print(f"Prueba {i}/{len(test_cases)} completada. Continuando...")
            print("-"*60)
    
    print("\n" + "="*60)
    print("PRUEBAS COMPLETADAS")
    print("="*60)
    print("\nRevisa las respuestas anteriores:")
    print("- Las preguntas sobre GEA deberian tener respuestas utiles")
    print("- Las preguntas fuera de contexto deberian decir 'no tengo informacion'")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()

