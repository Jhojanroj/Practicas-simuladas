# =========================================
# CLASE RESERVA
# =========================================

from excepciones import ErrorReserva

class Reserva:
    """Relaciona cliente con servicio"""

    def __init__(self, cliente, servicio, duracion):
        if duracion <= 0:
            raise ErrorReserva("La duración debe ser mayor a 0")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion

    def calcular_total(self):
        return self.servicio.calcular_costo(self.duracion)