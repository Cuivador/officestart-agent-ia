"""
=========================================================
Archivo principal de la aplicación.

Responsabilidad:
    Iniciar la aplicación y probar la lectura del
    Manual del Estudiante.
=========================================================
"""

from pathlib import Path
from src.pdf_loader import load_pdf

def main():
    """
    Funcion principal de la aplicacion
    """
    
    #Ruta al manual que utilizara el agente.
    pdf_path = Path("data/Manual_del_Estudiante_OfficeStart_v1.0.pdf")
    
    #Leer el contenido del PDF
    document_text = load_pdf(pdf_path)

    #Mostrar una vista previa del contenido (slicing de 0 hasta 1000).
    print(document_text[:1000])

if __name__ == "__main__":
    main()