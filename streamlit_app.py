import streamlit as st
from src.config import PDF_PATH
from src.pdf_loader import load_pdf
from src.llm import generate_response

@st.cache_data
def load_document():
    """
    Carga el Manual del Estudiante una unica vez y almacena el resultado
    en cache
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

        # Generar la respuesta del asistente
        with st.spinner("Procesando su solicitud..."):
            response = generate_response(
                document_text, 
                question
            )

        # Guardar la respuesta del asistente
        st.session_state["messages"].append(
            {
                "role": "assistant",
                "content": response 
            }
        )

        #Volver a ejecutar el script para actualizar el historial
        st.rerun()