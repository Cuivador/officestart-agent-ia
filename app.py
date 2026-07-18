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
from src.user_input import get_user_question
from time import perf_counter

def main():
    """
    Funcion principal de la aplicacion
    """
    
    #Leer el contenido del Manual del Estudiante
    document_text = load_pdf(PDF_PATH)
    #Mensaje de Bienvenida
    print("=" * 50)
    print("     Asistente Virtual de OfficeStart")
    print("=" * 50)
    print("Escribe tu pregunta sobre el Manual del Estudiante.")
    print("Para finalizar la conversacion escribe: salir\n")

    """
    Mantiene activa la conversacion con el usuario hasta que este decida finalizarla
    escribiendo la palabra clave "salir".
    """
    while True:
        # Optiene la pregunta del usuario
        question = get_user_question()
        # Verifica si la entrada es salir
        if question.strip().lower() == "salir":
            print("\nGracias por utilizar el Asistente Virtual de OfficeStart.")
            print("¡Hasta Pronto!")
            break

        # Informar al usuario que la consulta esta siendo procesada
        print("\nProcesando su pregunta...\n")

        # Iniciar la medicion del tiempo de respuesta
        start_time = perf_counter()

        # Generar la respuesta utilizando el contenido del manual.
        response = generate_response(document_text, question)

        # Finalizar la medicion del tiempo de respuesta
        end_time = perf_counter()

        # Calcular el tiempo que tardo el modelo en responder
        response_time = end_time - start_time

        # Mostrar la respuesta obtenida.
        print(response)

        # Mostrar el tiempo de respuesta
        print(f"Tiempo de respuesta: {response_time:.2f} segundos")
        print()
  
if __name__ == "__main__":
    main()