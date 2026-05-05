# =========================================
# PROGRAMA PRINCIPAL
# =========================================

from cliente import Cliente
from servicios import ReservaSala, AlquilerEquipo, Asesoria
from reserva import Reserva
from utils import guardar_log

def main():
    reservas = []

    try:
        cliente = Cliente("Jhojan", "123")

        s1 = ReservaSala("Sala")
        s2 = AlquilerEquipo("Equipos")
        s3 = Asesoria("Asesoría")

        r1 = Reserva(cliente, s1, 2)
        r2 = Reserva(cliente, s2, 3)
        r3 = Reserva(cliente, s3, 1)

        reservas.extend([r1, r2, r3])

        print(cliente)
        print("------ RESERVAS ------")

        for r in reservas:
            print(f"Servicio: {r.servicio.nombre}")
            print(f"Costo: {r.calcular_total()}")
            print("----------------------")

    except Exception as e:
        print("Error:", e)
        guardar_log(str(e))


if __name__ == "__main__":
    main()