"""
Este archivo indica que la carpeta 'src' forma parte de un paquete de 
Python.

Se mantiene aunque actualmente no contenga codigo, ya que es una buena 
practica de organización y facilita la estructura del proyecto.

Gracias a esta organizacion es posible importar modulos del paquete, por 
ejemplo:

    from src.user_input import get_user_question
    from src.pdf_loader import load_pdf
    from src.llm import generate_response

En proyectos mas grandes, este archivo tambien puede utilizarse para 
inicializar el paquete o exponer los modulos y funciones que se desean 
hacer publicos.
"""