"""
===============================================================
Módulo: llm.py

Responsabilidad:
    Gestionar la comunicación entre la aplicación y el
    modelo de inteligencia artificial Gemini.

Este modulo NO conoce el contenido del PDF ni interactúa
con la interfaz de usuario.

Su única responsabilidad es enviar solicitudes al modelo
y devolver las respuestas generadas.
===============================================================
"""

import os
from dotenv import load_dotenv
from google import genai
from src.config import MODEL_NAME

def get_api_key():
    """
        Obtiene la API Key de Gemini desde el archivo .env.
    Returns:
        str: API Key utilizada para autenticarse con Gemini.
    Raises:
        ValueError: Si la variable GEMINI_API_KEY no existe.
    """

    #Cargar las variables de entorno definidas en el archivo .env
    load_dotenv()

    #Obtener la API Key de Gemini desde las variables de entorno.
    api_key = os.getenv("GEMINI_API_KEY")

    #Verificar que la API Key exista
    if not api_key:
        raise ValueError(
            "No se encontró la variable de GEMINI_API_KEY en el archivo .env"
        )
    return api_key

def create_client():
    """
    Crea un cliente autenticado para comunicarse con Gemini.

    Returns:
        genai.Client: Cliente configurado para realizar solicitudes
        al modelo de IA.
    """

    #Obtener la API Key desde el archivo .env
    api_key = get_api_key()

    #Crear un cliente autenticado para Gemini
    client = genai.Client(api_key=api_key)

    return client

def build_prompt(context, question):
    """
    Construye el prompt que será enviado a Gemini.

    Args:
        context (str): Contenido del documento PDF.
        question (str): Pregunta realizada por el usuario.

    Returns:
        str: Prompt completo para enviar al modelo.
    """

    prompt = f"""
            Eres un asistente virtual de OfficeStart.

            Tu objetivo es ayudar a los estudiantes respondiendo únicamente
            preguntas basadas en la información contenida en el Manual del
            Estudiante de OfficeStart.

            Reglas:
            1. Responde únicamente con información presente en el manual.

            2. No inventes información ni completes respuestas utilizando conocimiento 
                externo.

            3. Si el manual contiene la información necesaria para responder,
                utilízala de forma clara sin modificar su significado.

            4. Si la respuesta se encuentra en varias partes del manual,
                combina la información para ofrecer una respuesta completa
                sin repetir contenido innecesariamente.

            5. Si la respuesta no se encuentra en el Manual del Estudiante, informa 
                amablemente al usuario que eres el asistente virtual de OfficeStart y que 
                solo puedes responder preguntas basadas en el contenido del manual. Invítalo 
                a realizar otra consulta relacionada con OfficeStart.

            6. Si la pregunta es ambigua o incompleta, solicita amablemente que el usuario 
                la reformule.

            7. Responde siempre en español.

            8. Utiliza un tono amable, claro y profesional.

            9. Organiza la respuesta de forma fácil de leer.

            Manual del Estudiante:
            ----------------------
            {context}
            
            Pregunta del usuario:
            {question}
            """
    return prompt

def generate_response(context, question):
    """
    Genera una respuesta utilizando el modelo Gemini

    Args:
        context (str): Contenido del Manual del Estudiante.
        question (str): Pregunta realizada por el usuario.

    Returns:
        str: Respuesta generada por Gemini
    """
    try:
        #Crear el cliente para comunicarse con Gemini
        client = create_client()

        #Construir el prompt con el contexto y la pregunta.
        prompt = build_prompt(context, question)

        #Enviar el prompt al modelo de Gemini.
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        #Devolver únicamente el texto de la respuesta.
        return response.text
    
    except Exception as error:
        # Convertir el error a texto para analizarlo
        error_message = str(error)

        # Mostrar el error en la consola
        print(error_message)

        # Error: Cuota de la API agotada
        if "429" in error_message:
            return (
                "⚠️ Se alcanzó el límite de solicitudes de la API de Gemini.\n\n"
                "Espere unos minutos e inténtelo nuevamente."
            )
        
        # Error: alta demanda del servicio
        elif "503" in error_message:
            return (
                "⚠️ Gemini está experimentando una alta demanda en este momento.\n\n"
                "Por favor, inténtelo nuevamente en unos instantes."
            )

        # Cualquier otro error
        else:
            return (
                "❌ Lo siento, ha ocurrido un error inesperado al procesar su solicitud.\n\n"
                "Por favor, inténtelo nuevamente en unos momentos."
            )