# =========================================
# MANEJO DE EXCEPCIONES PERSONALIZADAS
# =========================================

class ErrorSistema(Exception):
    """
    Clase base para todos los errores del sistema.
    Permite manejar excepciones personalizadas.
    """
    pass


class ErrorCliente(ErrorSistema):
    """
    Error cuando hay problemas con los datos del cliente.
    """
    pass


class ErrorReserva(ErrorSistema):
    """
    Error cuando hay problemas en la reserva.
    """
    pass