#---------------------- CLASE SUPERIOR VEHICULO ------------------------------------
class vehiculo:
    def __init__(self, placa, combustible):
        self.placa = placa
        self.combustible = combustible
    
    def mostrar(self):
        print("\n--- FICHA TECNICA ---")
        print(f"La placa del vehiculo es: {self.placa}")
        print(f"El tipo de combustible que usa el vehiculo es: {self.combustible}")

#--------------------- CLASE HIJA BUS -----------------------------------------------
class bus(vehiculo):
    def __init__(self, placa, combustible, capacidadp):
        super().__init__(placa, combustible)
        self.capacidadp = capacidadp

    def mostrar_bus(self):
        self.mostrar()
        print(f"La capacidad de pasajeros del bus es de: {self.capacidadp}")

#------------------ CLASE HIJA PATRULLA ---------------------------------------------
class patrulla(vehiculo):
    def __init__(self, placa, combustible, nivelb):
        super().__init__(placa, combustible)
        self.nivelb = nivelb

    def mostrar_patrulla(self):
        self.mostrar()
        print(f"El nivel de blindaje de la patrulla es: {self.nivelb}")

#-------------------- FUNCION DEL MENU PARA LA ACTIVACION HACIA EL USUARIO --------------
def menu():
    v1 = input("¿Que placa tiene su vehiculo? ->: ")
    v2 = input("¿Que tipo de combustible usa su vehiculo? ->: ")
    v3 = input("¿Que tipo de vehiculo es el suyo (bus/patrulla)? ->: ").lower()

    if v3 == "bus":
        capacidad = input("¿Que capacidad de pasajeros tiene su bus? ->: ")
        
        bus1 = bus(v1, v2, capacidad)
        bus1.mostrar_bus()

    elif v3 == "patrulla":
        blindaje = input("¿Que nivel de blindaje tiene su patrulla? ->: ")
        
        patrulla1 = patrulla(v1, v2, blindaje)
        patrulla1.mostrar_patrulla()

    else:
        print("Tipo de vehiculo no valido")


menu()
# ---------------- FIN DEL PROGRAMA ----------------------------------------------------