
# ================= CLASES =================

# Clases Juan Esteban
class Cafetera:
    def __init__(self,marca, modelo, tamaño, capacidad, temperaturaMaxEx, temperaturaMinEx, Material, tiempo_de_prepa ):
        self.marca = marca
        self.modelo = modelo
        self.tamaño = tamaño
        self.capacidad = capacidad
        self.temperaturaMaxEx = temperaturaMaxEx
        self.temperaturaMinEx = temperaturaMinEx
        self.Material = Material
        self.tiempo_de_prepa = tiempo_de_prepa
        
class Placa_Calefactora:
    def __init__(self,TemperaturaMax, PasodeCo, Estado ):
        self.TemperaturaMax = TemperaturaMax
        self.PasodeCo = PasodeCo
        self.Estado = Estado

class Resistencia:
    def __init__(self,Potencia, Voltaje, Estado, Temperatura):
        self.Potencia = Potencia
        self.Voltaje = Voltaje
        self.Estado = Estado
        self.Temperatura = Temperatura
        
# Clases Jeremy Patiño
class deposito:
    def __init__(self, tamaño, capacidad ):
        self.tamaño = tamaño
        self.capacidad = capacidad
        
class sensor:
    def __init__(self, tipo_sensor, nivel_exactitud, unidad_medida, medidas_comparacion):
        self.tipo_sensor = tipo_sensor
        self.nivel_exactitud = nivel_exactitud
        self.unidad_medida = unidad_medida
        self.medidas_comparacion = medidas_comparacion
        
class Filtro:
    def __init__(self, tipo, capacidad, densidad, material):
        self.tipo = tipo
        self.capacidad = capacidad
        self.densidad = densidad
        self.material = material

# Clases Edward Suarez
class goteo:
    def __init__(self,cantidadagua):
        self.cantidad = cantidadagua
    
class jarra:
    def __init__(self,capacidad, nivel_lleno):
        self.capacidad = capacidad
        self.nivelleno = nivel_lleno
        
class indicador:
    def __init__(self, tipo, estado):
        self.tipo = tipo
        self.estado = estado


# ================= OBJETOS =================

cafetera1 = Cafetera("Oster", "BVSTEM7301", "34.5 cm ×27.8 cm ×30 cm", "2.8 litros", "96 °C",  "88 °C", "ACERO Y PLASTICO", "3-4 MINUTOS")

Placa1 = Placa_Calefactora("55° y 60°", "1380W - 1450W ", "Encendido/Apagado")

Resis1 = Resistencia("1380W - 1450W", "120v", "Encendido/Apagado", "88°C - 96°C")

deposito1 = deposito ("23.5cm * 22.5cm * 6cm", "2.8 litros")

sensor1 = sensor ("nivel de agua","100%", "mililitros", "mililitros")
sensor2 = sensor ("nivel de peso", "85%", "gramos", "gramos")

filtro1 = Filtro ("filtro de canasta", "10-12 tazas", "8.0 g/cm³", "acero inoxidable")

jarra1 = jarra("600 ml", "80%")


# ================= FUNCIONES =================

def encendido():
    while True:
        en = input("¿La cafetera está conectada a corriente? (S/N): ").strip().upper()
        
        if en == "S":
            return True
        elif en == "N":
            print("Por favor conecta la cafetera.")
        else:
            print("Opción no válida")


def pedir_nombre():
    nombre = ""
    while not nombre.strip():
        nombre = input("Ingresa tu nombre de usuario: ").strip()
    
    return nombre


def comprobar_agua(sensor_agua):
    print(f"Sensor utilizado: {sensor_agua.tipo_sensor}")
    
    while True:
        respuesta = input("¿El depósito tiene agua? (S/N): ").strip().upper()
        
        if respuesta == "S":
            print("✔ Hay agua suficiente.")
            return True
        elif respuesta == "N":
            print("❌ No hay agua.")
            return False
        else:
            print("Opción no válida")


def llenar_jarra(jarra_obj):
    while True:
        try:
            nivel = int(input("Ingresa el nivel de la jarra (0 a 100): "))
            
            if 0 <= nivel <= 100:
                jarra_obj.nivelleno = f"{nivel}%"
                print(f"Nivel actualizado: {jarra_obj.nivelleno}")
                return
            else:
                print("El nivel debe estar entre 0 y 100.")
        
        except ValueError:
            print("Ingresa un número válido.")


def comprobar_jarra(jarra_obj, sensor_peso):
    print(f"Sensor utilizado: {sensor_peso.tipo_sensor}")
    print(f"Exactitud: {sensor_peso.nivel_exactitud}")
    
    print(f"Capacidad de la jarra: {jarra_obj.capacidad}")
    print(f"Nivel actual: {jarra_obj.nivelleno}")
    
    nivel = int(jarra_obj.nivelleno.replace("%", ""))
    
    while True:
        respuesta = input("¿El sensor detecta la jarra colocada? (S/N): ").strip().upper()
        
        if respuesta == "S":
            if nivel >= 90:
                print("⚠ La jarra está demasiado llena.")
                return False
            elif nivel <= 10:
                print("⚠ La jarra está muy vacía.")
                return False
            else:
                print("✔ Jarra detectada y en nivel adecuado.")
                return True
        
        elif respuesta == "N":
            print("❌ El sensor no detecta la jarra. Colócala correctamente.")
            return False
        
        else:
            print("Opción no válida.")


def iniciar_cafetera():
    print("☕ La cafetera está en funcionamiento...")


# ================= MAIN =================

def main():
    print("------ SISTEMA DE CAFETERA ------")
    
    if not encendido():
        return
    
    nombre = pedir_nombre()
    print(f"Hola, {nombre}! Bienvenido.")
    
    if not comprobar_agua(sensor1):
        print("No se puede iniciar sin agua 🚫")
        return
    
    llenar_jarra(jarra1)
    
    if not comprobar_jarra(jarra1, sensor2):
        print("No se puede iniciar por problema con la jarra 🚫")
        return
    
    iniciar_cafetera()


# ================= EJECUCIÓN =================

main()