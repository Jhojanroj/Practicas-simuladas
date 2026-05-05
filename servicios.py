# =========================================
# SERVICIOS (ABSTRACCIÓN + POLIMORFISMO)
# =========================================

from abc import ABC, abstractmethod

class Servicio(ABC):
    """Clase abstracta base"""

    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_costo(self, duracion, descuento=0):
        pass


class ReservaSala(Servicio):
    def calcular_costo(self, duracion, descuento=0):
        costo = duracion * 50000
        return costo - (costo * descuento)


class AlquilerEquipo(Servicio):
    def calcular_costo(self, duracion, descuento=0):
        costo = duracion * 30000
        return costo - (costo * descuento)


class Asesoria(Servicio):
    def calcular_costo(self, duracion, descuento=0):
        costo = duracion * 80000
        return costo - (costo * descuento)