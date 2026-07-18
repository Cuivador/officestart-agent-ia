"""
===============================================================
Modulo: pdf_loader.py

Responsabilidad:
    Leer el manual del estudiante en formato PDF, extraer su
    contenido y normalizar el texto para facilitar su procesamiento
    por el agente inteligentes.

Este módulo NO contiene lógica de inteligencia artificial.
Su única responsabilidad es obtener y preparar el contenido del
documento para que otros modulos puedan utilizarlo.
===============================================================
"""

from pathlib import Path
from pypdf import PdfReader

def clean_text(text: str) -> str:
    """
    Limpia el texto extraido del PDF para facilitar su procesamiento.
    """

    #Reemplazar saltos de linea por espacios.
    text = text.replace("\n", " ")

    #Normalizar espacios en blanco consecutivos.
    text = " ".join(text.split())
    return text

def load_pdf(pdf_path: Path) ->str:
    """
    Lee un archivo PDF y devuelve todo su contenido como una cadena
    de texto.

    Args:
        pdf_path (Path): Ruta del documento PDF.
        pdf_path -> Es el parámetro.
        : Path -> anotación de tipo (type hint)(recibir un objeto de tipo Path).

    Returns:
        str: Texto extraído del documento.
    """
    try:
        #Crear un lector para acceder al contenido del PDF - guarda un objeto
        reader = PdfReader(pdf_path)

        #Almacenará el texto completo del documento.
        text = ""

        #Recorrer cada una de las paginas del documento.
        for page in reader.pages:
            #Extraer el texto de la pagina actual y añadirlo al texto completo si no hay texto utiliza cadena vacia.
            text += page.extract_text() or ""
        #Devolver el texto completo del documento.
        return clean_text(text)

    #Informar cuando el archivo PDF no existe en la ruta indicada.
    except FileNotFoundError:
        raise FileNotFoundError(
            f"No se encontro el archivo PDF: {pdf_path}"
        ) from None
    
    #Capturar cualquier otro error inesperado durante la lectura del documento.
    except Exception as error:
        raise RuntimeError(
            f"Ocurrio un error al leer el PDF: {error}"
        ) from error