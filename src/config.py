"""
===============================================================
Modulo: config.py
Responsabilidad:
    Centralizar la configuracion general del proyecto,
    como rutas de archivos y parametros compartidos por
    los diferentes modulos.

Este modulo no contiene logica de negocio.
Su unica responsabilidad es proporcionar valores de
configuracion al resto de la aplicacion.
===============================================================
"""

from pathlib import Path

# Directorio raiz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

#Ruta al Manual del Estudiante.
PDF_PATH = BASE_DIR/"data"/"Manual_del_Estudiante_OfficeStart_v1.0.pdf"

#Modelo de Gemini que utilizara el proyecto
MODEL_NAME = "gemini-3.5-flash"