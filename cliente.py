# =========================================
# CLASE CLIENTE
# =========================================

from excepciones import ErrorCliente

class Cliente:
    """Representa un cliente del sistema"""

    def __init__(self, nombre, identificacion):
        if not nombre.strip():
            raise ErrorCliente("El nombre no puede estar vacío")

        self.nombre = nombre
        self.identificacion = identificacion

    def __str__(self):
        return f"Cliente: {self.nombre} - ID: {self.identificacion}"