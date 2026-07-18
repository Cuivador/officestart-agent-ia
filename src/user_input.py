"""
==============================================================
Modulo: user_input.py

Responsabilidad:
    Capturar y validar la pregunta ingresada por el usuario desde
    la consola.

Este modulo unicamente gestiona la interaccion con el usario
para obtener la pregunta que sera enviada al asistente
==============================================================
"""

def get_user_question():
    """
    Solicita al usuario una pregunta sobre el Manual del estudiante.

    Returns:
        str: Pregunta ingresada por el usuario
    """

    #solicitar al usuario una pregunta.
    question = input("Escribe tu pregunta: ")

    #Devolver la pregunta capturada.
    return question