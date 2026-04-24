#Clases Juan Esteban
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
        
#Clases Jeremy Patiño
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

#Clases Edward Suarez
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

#Variables de las Clases
cafetera1 = Cafetera("Oster", "BVSTEM7301", "34.5 cm ×27.8 cm ×30 cm", "2.8 litros", "96 °C",  "88 °C", "ACERO Y PLASTICO", "3 0 4 MINUTOS")

Placa1 = Placa_Calefactora("55° y 60°", "1380W - 1450W ", "Encendido/Apagado")

Resis1 = Resistencia("1380W - 1450W", "120v", "Encendido/Apagado", "88°C - 96°C")

deposito1 = deposito ("23.5cm * 22.5cm * 6cm", "2.8 litros")

sensor1 = sensor ("nivel de agua","100%", "mililitros", "mililitros")
sensor2 = sensor ("nivel de peso", "85%", "gramos", "gramos")
sensor3 = sensor ("nivel de temperatura","98.9%", "°C", "°C")
sensor4 = sensor ("nivel de presion","90%", "Bares", "Bares")

filtro1 = Filtro ("filtro de canasta", "10-12 tazas", "8.0 g/cm³", "acero inoxidable")

goteo1 = goteo("30 ml")
goteo2 = goteo("50 ml")

jarra1 = jarra("600 ml", "80%")
jarra2 = jarra("700 ml", "70%")

indicador1 = indicador("Sonoro", "Encendido")
indicador2 = indicador("Visual", "Apagado")

#prints de las clases
#print(cafetera1.marca, cafetera1.modelo, cafetera1.tamaño, cafetera1.capacidad, cafetera1.temperaturaMaxEx, cafetera1.temperaturaMinEx, cafetera1.Material, cafetera1.tiempo_de_prepa, sep="\n")
#print(Placa1.TemperaturaMax, Placa1.PasodeCo, Placa1.Estado, sep="\n")
#print(Resis1.Potencia, Resis1.Voltaje, Resis1.Estado, Resis1.Temperatura, sep="\n")
#print("la cafetera:",cafetera1.modelo,"de la marca: ",cafetera1.marca,"tiene una resistencia cuya potencia es: ",Resis1.Potencia,"Y una placa calefactora cuya Temperatura es: ",Placa1.TemperaturaMax, sep="\n")

#print(sensor1.tipo_sensor, sensor1.nivel_exactitud, sensor1.unidad_medida, sensor1.medidas_comparacion, sep="\n")
#print("\n", sensor2.tipo_sensor, sensor2.nivel_exactitud, sensor2.unidad_medida, sensor2.medidas_comparacion, sep="\n")
#print("\n", sensor3.tipo_sensor, sensor3.nivel_exactitud, sensor3.unidad_medida, sensor3.medidas_comparacion, sep="\n")
#print("\n", sensor4.tipo_sensor, sensor4.nivel_exactitud, sensor4.unidad_medida, sensor4.medidas_comparacion, sep="\n")
#print ("---------------------------------------------------------------------------------------------------------------------")
#print("\n", deposito1.capacidad, deposito1.tamaño , sep="\n")
#print ("--------------------------------------------------------------------------------------------------------------------")
#print("\n", filtro1.tipo, filtro1.capacidad, filtro1.material, filtro1.densidad, sep="\n")

#print("Goteo 1", goteo1.cantidad, sep="\n")
#print("\nGoteo 2", goteo2.cantidad, sep="\n")
#print("-------------------")

#print("Jarra 1", jarra1.capacidad, jarra1.nivelleno, sep="\n")
#print("\nJarra 2", jarra2.capacidad, jarra2.nivelleno, sep="\n")
#print("-------------------")

#print("Indicador 1", indicador1.tipo, indicador1.estado, sep="\n")
#print("\nIndicador 2", indicador2.tipo, indicador2.estado, sep="\n")
#print("-------------------")

def encendido():
    while True:
        en = input("¿Desea encender la cafetera? S/N: ")
        
        if en == "S":
            inicio()
            break
        elif en == "N":
            print("La cafetera sigue apagada.")
        else:
            print("Opción no válida")

def inicio():
    comp_cafe=input("¿El deposito tiene agua y cafe? S/N :")
    
encendido()