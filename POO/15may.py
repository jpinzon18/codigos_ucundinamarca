#-----------------------------------------------------------------
#Construimos la clase padre: Computador.
#Todos los computadores, sin importar la marca, tienen una referencia, procesador, RAM y disco.
#-------------------------------------------------------------------
class Computador:
    def __init__(self, referencia, microprocesador, memoria, disco): 
        self.marcas = referencia
        self.procesador = microprocesador  
        self.ram = memoria
        self.ssd = disco
 
    def mostrar(self):
        print(f"\n--- Ficha Técnica ---")
        print(f"Marca: {self.marcas}")
        print(f"Procesador: {self.procesador}")
        print(f"Memoria RAM: {self.ram}")
        print(f"Disco SSD: {self.ssd}")
 
# ---------------------------------------------------------------------- 
# SUBCLASE clase hija:Apple
# ---------------------------------------------------------------------
class Apple(Computador):
    def __init__(self, referencia, microprocesador, memoria, disco, chip_grafico):
        # --------------------------------------------------------------
        # ya que esta clase es hija de Computador, primero ve al padre y llena 
        # los datos básicos (referencia, procesador, etc.) para que yo no tenga 
        # que volver a escribirlos aquí", con la función super().
        #----------------------------------------------------------------
        super().__init__(referencia, microprocesador, memoria, disco)
        # --------------------------------------
        # Atributo exclusivo de la hija: Apple
        #--------------------------------------
        self.graficos = chip_grafico
 
    def mostrar_apple(self):
        self.mostrar() # Usa el método del padre
        print(f"Gráficos: {self.graficos}")
        print("Ecosistema: macOS compatible.")
 
# ---------------------------------------------------------------------- 
# SUBCLASE clase hija:DELL
# ---------------------------------------------------------------------
class Dell(Computador):
    def __init__(self, referencia, microprocesador, memoria, disco, garantia_meses):
        super().__init__(referencia, microprocesador, memoria, disco)
        # --------------------------------------
        # Atributo exclusivo de la hija: DELL
        #--------------------------------------
        self.garantia = garantia_meses
 
    def mostrar_dell(self):
        self.mostrar() # Usa el método del padre
        print(f"Soporte: {self.garantia} meses de garantía ProSupport.")

#SUB CLASE ASUS
class Asus(Computador):
    def __init__(self, referencia, microprocesador, memoria, disco, tipoplaca):
        super().__init__(referencia, microprocesador, memoria, disco, tipoplaca)

        self.tipop = tipoplaca
    
    def mostrar_asus(self):
        self.mostrar()
        print(f"el tipo de placa es: {self.tipop}")
 
# --- LÓGICA DE USUARIO ---
marca = input("¿Qué marca de computador estás usando? (Apple/Dell): ").capitalize()
ref = input("Referencia (ej: MacBook Pro / Latitude): ")
cpu = input("¿Qué microprocesador tiene?: ")
ram = input("¿Capacidad de memoria?: ")
hdd = input("¿Capacidad de disco?: ")
 
if marca == "Apple":
    chip = input("¿Qué chip gráfico tiene (ej: M2 de 10 núcleos)?: ")
    mi_equipo = Apple(ref, cpu, ram, hdd, chip)
    mi_equipo.mostrar_apple()
elif marca == "Dell":
    meses = input("¿Cuántos meses de garantía tiene?: ")
    mi_equipo = Dell(ref, cpu, ram, hdd, meses)
    mi_equipo.mostrar_dell()
else:
    # Si no es ninguna marca especial, usamos la clase base general
    mi_equipo = Computador(ref, cpu, ram, hdd)
    mi_equipo.mostrar()