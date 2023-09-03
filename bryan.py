hola papu ya llego papa
pcnqwknxwqkx
print("cuebqjqBNKNCOSNAAS")
class Nota:
    def __init__(self, folio, fecha, cliente):
         # Constructor de la clase Nota
        self.folio = folio  # Número de folio de la nota
        self.fecha = fecha  # Fecha de la nota
        self.cliente = cliente  # Nombre del cliente
        self.servicios = []  # Lista de servicios en la nota
        self.monto_total = 0.0  # Monto total de la nota
        self.cancelada = False  # Estado de cancelación de la nota

    def agregar_servicio(self, nombre_servicio, costo_servicio):
        try:
            # Intenta convertir el costo del servicio en un número decimal (float)
            costo_servicio = float(costo_servicio)
            # Agrega el servicio a la lista de servicios y actualiza el monto total
            self.servicios.append((nombre_servicio, costo_servicio))
            self.monto_total += costo_servicio
        except ValueError:
            print("Error: El costo del servicio debe ser un número válido.")
