"""
===============================================================
Módulo: llm.py

Responsabilidad:
    Gestionar la comunicacion entre la aplicacion y el
    modelo de inteligencia artificial Gemini.

Este modulo NO conoce el contenido del PDF ni interactua
con la interfaz de usuario.

Su unica responsabilidad es enviar solicitudes al modelo
y devolver las respuestas generadas.
===============================================================
"""

import os
from dotenv import load_dotenv
from google import genai

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
            "No se encontro la variable de GEMINI_API_KEY en el archivo .env"
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
