from abc import ABC, abstractmethod

# ==============================
# EXCEPCIONES PERSONALIZADAS
# ==============================
class ErrorSistema(Exception):
    pass

class ErrorCliente(ErrorSistema):
    pass

class ErrorReserva(ErrorSistema):
    pass


# ==============================
# CLASE ABSTRACTA BASE
# ==============================
class Entidad(ABC):
    
    @abstractmethod
    def mostrar_info(self):
        pass


# ==============================
# CLASE CLIENTE
# ==============================
class Cliente(Entidad):
    
    def __init__(self, nombre, identificacion, correo):
        if not nombre or not correo:
            raise ErrorCliente("Datos del cliente inválidos")
        
        self._nombre = nombre
        self._identificacion = identificacion
        self._correo = correo
    
    def mostrar_info(self):
        return f"Cliente: {self._nombre} - ID: {self._identificacion}"


# ==============================
# CLASE ABSTRACTA SERVICIO
# ==============================
class Servicio(ABC):
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    @abstractmethod
    def calcular_costo(self, duracion, descuento=0):
        pass


