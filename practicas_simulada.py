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


# ==============================
# SERVICIOS (POLIMORFISMO)
# ==============================
class ReservaSala(Servicio):
    
    def calcular_costo(self, duracion, descuento=0):
        costo = duracion * 50
        return costo - (costo * descuento)


class AlquilerEquipo(Servicio):
    
    def calcular_costo(self, duracion, descuento=0):
        costo = duracion * 30
        return costo - (costo * descuento)


class Asesoria(Servicio):
    
    def calcular_costo(self, duracion, descuento=0):
        costo = duracion * 100
        return costo - (costo * descuento)


# ==============================
# CLASE RESERVA
# ==============================
class Reserva:
    
    def __init__(self, cliente, servicio, duracion):
        if duracion <= 0:
            raise ErrorReserva("Duración inválida")
        
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"
    
    def confirmar(self):
        self.estado = "Confirmada"
    
    def cancelar(self):
        self.estado = "Cancelada"
    
    def calcular_total(self, descuento=0):
        return self.servicio.calcular_costo(self.duracion, descuento)


# ==============================
# LOGS
# ==============================
def guardar_error(error):
    with open("logs.txt", "a") as f:
        f.write(str(error) + "\n")


# ==============================
# SIMULACIÓN
# ==============================
print("=== SISTEMA SOFTWARE FJ ===")

clientes = []
reservas = []

# 1
try:
    c1 = Cliente("Jhojan", "123", "correo@gmail.com")
    clientes.append(c1)
except Exception as e:
    guardar_error(e)

# 2
try:
    c2 = Cliente("", "456", "")
except ErrorCliente as e:
    print("Error cliente:", e)
    guardar_error(e)

# 3
try:
    servicio1 = ReservaSala("Sala VIP")
    r1 = Reserva(c1, servicio1, 2)
except Exception as e:
    guardar_error(e)
else:
    r1.confirmar()
    reservas.append(r1)
    print("Reserva confirmada:", r1.calcular_total())
finally:
    print("Proceso 3 finalizado")

# 4
try:
    r2 = Reserva(c1, servicio1, -1)
except ErrorReserva as e:
    print("Error reserva:", e)
    guardar_error(e)

# 5
try:
    servicio2 = AlquilerEquipo("Laptop")
    r3 = Reserva(c1, servicio2, 3)
    print("Total alquiler:", r3.calcular_total(0.1))
except Exception as e:
    guardar_error(e)

# 6
try:
    servicio3 = Asesoria("Consultoría")
    r4 = Reserva(c1, servicio3, 1)
    print("Total asesoría:", r4.calcular_total())
except Exception as e:
    guardar_error(e)

# 7
try:
    r3.confirmar()
    print("Estado:", r3.estado)
except Exception as e:
    guardar_error(e)

# 8
try:
    r1.cancelar()
    print("Estado:", r1.estado)
except Exception as e:
    guardar_error(e)

# 9
try:
    raise ErrorSistema("Error general del sistema")
except ErrorSistema as e:
    print("Error detectado:", e)
    guardar_error(e)

# 10
try:
    c3 = Cliente("Ana", "789", "ana@gmail.com")
    servicio4 = ReservaSala("Sala normal")
    r5 = Reserva(c3, servicio4, 4)
    print("Reserva final:", r5.calcular_total())
except Exception as e:
    guardar_error(e)