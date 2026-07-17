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

def main():
    """
    Funcion principal de la aplicacion
    """
    
    #Leer el contenido del Manual del Estudiante
    document_text = load_pdf(PDF_PATH)

    #Mostrar una vista previa del contenido (slicing de 0 hasta 1000).
    print(document_text[:1000])

if __name__ == "__main__":
    main()