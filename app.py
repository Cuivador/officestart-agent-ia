"""
=========================================================
Archivo principal de la aplicación.

Responsabilidad:
    Iniciar la aplicación y probar la lectura del
    Manual del Estudiante.
=========================================================
"""

from src.config import PDF_PATH
from src.pdf_loader import load_pdf
from src.llm import generate_response

def main():
    """
    Funcion principal de la aplicacion
    """
    
    #Leer el contenido del Manual del Estudiante
    document_text = load_pdf(PDF_PATH)
    
    # Pregunta de prueba para verificar la comunicación con Gemini.
    question = "¿Que cursos?"
    # Generar la respuesta utilizando el contenido del manual.
    response = generate_response(document_text, question)
    # Mostrar la respuesta obtenida.
    print(response)

if __name__ == "__main__":
    main()