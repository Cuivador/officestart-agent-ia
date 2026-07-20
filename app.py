"""
===============================================================
Módulo: app.py

Responsabilidad:
    Implementar la interfaz conversacional del agente
    OfficeStart Agent IA mediante Streamlit.

Este módulo coordina la interacción con el usuario,
gestiona el historial de conversación, controla el flujo
de la aplicación y delega la carga del documento y la
generación de respuestas a los módulos especializados.
===============================================================
"""

import streamlit as st
from src.config import PDF_PATH
from src.pdf_loader import load_pdf
from src.llm import generate_response
from time import perf_counter

@st.cache_data
def load_document():
    
    """
    Carga el Manual del Estudiante y almacena su contenido en la
    caché de Streamlit para evitar lecturas repetidas del archivo.

    Returns:
        str: Contenido completo del Manual del Estudiante.
    """
    return load_pdf(PDF_PATH)

document_text = load_document()

# Crear el historial de conversacion si aun no existe
if "messages" not in st.session_state:
    st.session_state["messages"] = []

st.title("🤖 Asistente Virtual OfficeStart v1.0")

st.write(
    "Realiza preguntas sobre el Manual del Estudiante "
    "y obten respuestas basadas en su contenido."
)

st.info("¡Bienvenido! Escribe una pregunta para comenzar.")

# Mostrar el historial de la conversacion
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.write(message["content"])
        if message["role"] == "assistant":
            st.caption(
                f"⏱ Tiempo de respuesta: {message['response_time']:.2f} segundos"
            )
        

# Mostrar el botton unicamente cuando exista una conversacion
if st.session_state["messages"]:

    # Limpiar el historial de conversacion
    if st.button("🗑️ Limpiar conversación"):
        st.session_state["messages"].clear()
        st.rerun()

# Cuadro para escribir una nueva pregunta
question = st.chat_input("Escribe tu pregunta...")

# Verificar si el usuario ha enviado una pregunta
if question is not None:

    # Validar si la pregunta contiene unicamente espacios
    if question.strip() == "":
        st.warning("Lo siento, no has escrito ninguna pregunta.")

    else:
        # Guardar la pregunta del usuario
        st.session_state["messages"].append(
            {
                "role": "user",
                "content": question 
            }
        )

        # Iniciar la medicion del tiempo de respuesta
        start_time = perf_counter()

        # Generar la respuesta del asistente
        with st.spinner("Procesando su solicitud..."):
            response = generate_response(
                document_text, 
                question
            )

        # Finalizar la medicion del tiempo de respuesta
        end_time = perf_counter()

        # Calcular el tiempo que tardo el modelo en responder
        response_time = end_time - start_time

        # Guardar la respuesta del asistente
        st.session_state["messages"].append(
            {
                "role": "assistant",
                "content": response,
                "response_time": response_time
            }
        )

        #Volver a ejecutar el script para actualizar el historial
        st.rerun()