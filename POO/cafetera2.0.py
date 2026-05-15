# ================= CLASES =================

class Cafetera:  #definiendo clase general de la cafetera
    def __init__(self,marca, modelo, tamaño, capacidad, temperaturaMaxEx, temperaturaMinEx, Material, tiempo_de_prepa ):
        self.marca = marca
        self.modelo = modelo
        self.tamaño = tamaño
        self.capacidad = capacidad
        self.temperaturaMaxEx = temperaturaMaxEx
        self.temperaturaMinEx = temperaturaMinEx
        self.Material = Material
        self.tiempo_de_prepa = tiempo_de_prepa
        
class Placa_Calefactora: #definiendo clase de la placa calefactora
    def __init__(self,TemperaturaMax, PasodeCo, Estado ):
        self.TemperaturaMax = TemperaturaMax
        self.PasodeCo = PasodeCo
        self.Estado = Estado

class Resistencia: #definiendo clase de la resistencia
    def __init__(self,Potencia, Voltaje, Estado, Temperatura):
        self.Potencia = Potencia
        self.Voltaje = Voltaje
        self.Estado = Estado
        self.Temperatura = Temperatura
        
class deposito:  #definiendo clase del deposito
    def __init__(self, tamaño, capacidad ):
        self.tamaño = tamaño
        self.capacidad = capacidad
        
class sensor:   #definiendo clase de los sensores
    def __init__(self, tipo_sensor, nivel_exactitud, unidad_medida, medidas_comparacion):
        self.tipo_sensor = tipo_sensor
        self.nivel_exactitud = nivel_exactitud
        self.unidad_medida = unidad_medida
        self.medidas_comparacion = medidas_comparacion
        
class Filtro:  #definiendo clase del filtro
    def __init__(self, tipo, capacidad, densidad, material):
        self.tipo = tipo
        self.capacidad = capacidad
        self.densidad = densidad
        self.material = material

class goteo:  #definiendo clase de goteo
    def __init__(self,cantidadagua):
        self.cantidad = cantidadagua
    
class jarra: #definiendo clases de la jarra
    def __init__(self,capacidad, nivel_lleno):
        self.capacidad = capacidad
        self.nivelleno = nivel_lleno
        
class indicador: #definiendo clase indicador
    def __init__(self, tipo, estado):
        self.tipo = tipo
        self.estado = estado


# =================DEFINICION DE LOS OBJETOS =================
#se define el objeto de la clase cafetera
cafetera1 = Cafetera("Oster", "BVSTEM7301", "34.5 cm ×27.8 cm ×30 cm", "2.8 litros", "96 °C",  "88 °C", "ACERO Y PLASTICO", "3-4 MINUTOS")

#se define el objeto de la clase placa calefactora
Placa1 = Placa_Calefactora("55° y 60°", "1380W - 1450W ", "Encendido/Apagado")

#se define el objeto de la clase resistencia 
Resis1 = Resistencia("1380W - 1450W", "120v", "Encendido/Apagado", "88°C - 96°C")

#se define el objeto de la clase deposito
deposito1 = deposito ("23.5cm * 22.5cm * 6cm", "2.8 litros")

#se definen los objetos de la clase de sensor en este caso de agua y de peso
sensor1 = sensor ("nivel de agua","100%", "mililitros", "mililitros")
sensor2 = sensor ("nivel de peso", "85%", "gramos", "gramos")

#se define el objeto que hace uso de la clase filtro
filtro1 = Filtro ("filtro de canasta", "10-12 tazas", "8.0 g/cm³", "acero inoxidable")

#se define el objeto que hace uso de la clase jarra
jarra1 = jarra("600 ml", "80%")

# =================DEFINICION DE LAS FUNCIONES =================
#SE DEFINE LA FUNCION DE ENCENDIDO
def encendido():
    while True:
        en = input("¿La cafetera está conectada a corriente? (S/N): ").strip().upper()
        
        if en == "S":
            return True
        elif en == "N":
            print("Por favor conecta la cafetera.")
        else:
            print("Opción no válida")

#SE DEFINE LA FUNCION DONDE SE PIDE NOMBRE DE USUARIO
def pedir_nombre():
    nombre = ""
    while not nombre.strip():
        nombre = input("Ingresa tu nombre de usuario: ").strip()
    
    return nombre

#SE DEFINE LA FUNCION PARA COMPROBAR SI EL DEPOSITO TIENE AGUA
def comprobar_agua(sensor_agua):
    print(f"\nSensor utilizado: {sensor_agua.tipo_sensor}")
    
    while True:
        respuesta = input("¿El depósito tiene agua? (S/N): ").strip().upper()
        
        if respuesta == "S":
            print("Hay agua suficiente.")
            return True
        elif respuesta == "N":
            print("No hay agua.")
            print("Agrega agua para continuar el proceso.")
            return comprobar_agua(sensor1)
        else:
            print("Opción no válida")

#SE DEFINE LA FUNCION PARA COMPROBAR EL NIVEL ACTUAL DE CONTENIDO QUE TIENE LA JARRA
def llenar_jarra(jarra_obj):
    while True:
        try:
            nivel = int(input("\nIngresa el nivel de la jarra (0 a 100): "))
            
            if 0 <= nivel <= 100:
                jarra_obj.nivelleno = f"{nivel}%"
                print(f"Nivel actualizado: {jarra_obj.nivelleno}")
                return
            else:
                print("El nivel debe estar entre 0 y 100.")
        
        except ValueError:
            print("Ingresa un número válido.")

#SE DEFINE LA FUNCION DONDE SE COMPRUEBA QUE LA JARRA ESTE EN UNA POSICION CORRECTA
def comprobar_jarra(jarra_obj, sensor_peso):
    print(f"Sensor utilizado: {sensor_peso.tipo_sensor}")
    print(f"Exactitud: {sensor_peso.nivel_exactitud}")
    
    print(f"Capacidad de la jarra: {jarra_obj.capacidad}")
    print(f"Nivel actual: {jarra_obj.nivelleno}")
    
    nivel = int(jarra_obj.nivelleno.replace("%", ""))
    
    while True:
        respuesta = input("\n¿El sensor detecta la jarra colocada? (S/N): ").strip().upper()
        
        if respuesta == "S":
            if nivel >= 90:
                print(" La jarra está demasiado llena.")
                return False
            elif nivel <= 10:
                print(" La jarra está muy vacía.")
                return False
            else:
                print(" Jarra detectada y en nivel adecuado.")
                return True
        elif respuesta == "N":
            print("El sensor no detecta la jarra. Colócala correctamente.")
            comprobar_jarra(jarra1, sensor2)
        else:
            print("Opción no válida.")


#SE DEFINE LA FUNCION PARA VERIFICAR QUE TODOS LOS SISTEMAS ANTERIORES ESTAN CORRECTOS
def verificacion():
    while True:
        respuesta = input("\n¿Todo se verifico correctamente? (S/N): ").strip().upper()
        
        if respuesta == "S":
            print("Se iniciara el proceso de preparación...")
            return False
        elif respuesta == "N":
            print("Entrando en modo seguro...(Apagando)")
            exit()
        else:
            print("Opción no válida")
            verificacion()

#SE DEFINE LA FUNCION DONDE COMIENZA LA PREPARACION
def iniciar_cafetera():
    print("\nLa cafetera está en funcionamiento...")

# =================DEFINICION DE LA FUNCION MAIN =================
def main():
    print("------ SISTEMA DE CAFETERA ------")
    
    if not encendido():
        return
    
    nombre = pedir_nombre()
    print(f"Hola, {nombre}! Bienvenido.")
    
    if not comprobar_agua(sensor1):
        print("No se puede iniciar sin agua ")
        return     
    llenar_jarra(jarra1)
    
    if not comprobar_jarra(jarra1, sensor2):
        print("No se puede iniciar por problema con la jarra ")
        return
    verificacion()
    
    iniciar_cafetera()

# ================= LINEAS DE EJECUCIÓN =================

main()