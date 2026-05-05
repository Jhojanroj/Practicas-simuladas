# =========================================
# UTILIDADES DEL SISTEMA
# =========================================

from datetime import datetime

def guardar_log(mensaje):
    """
    Guarda mensajes de error en un archivo logs.txt
    """
    with open("logs.txt", "a") as archivo:
        archivo.write(f"{datetime.now()} - {mensaje}\n")