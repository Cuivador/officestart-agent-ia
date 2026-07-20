"""
===============================================================
Modulo: config.py
Responsabilidad:
    Centralizar la configuración general del proyecto,
    como rutas de archivos y parámetros compartidos por
    los diferentes módulos.

Este modulo no contiene lógica de negocio.
Su única responsabilidad es proporcionar valores de
configuración al resto de la aplicación.
===============================================================
"""

from pathlib import Path

# Directorio raíz del proyecto.
BASE_DIR = Path(__file__).resolve().parent.parent

#Ruta al Manual del Estudiante.
PDF_PATH = BASE_DIR/"data"/"Manual_del_Estudiante_OfficeStart_v1.0.pdf"

#Modelo de Gemini que utilizara el proyecto.
MODEL_NAME = "gemini-3.5-flash"