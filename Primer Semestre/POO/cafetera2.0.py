# ================= CLASES =================

class Cafetera:  # definiendo clase general de la cafetera
    def __init__(self, marca, modelo, tamaño, capacidad,
                 temperaturaMaxEx, temperaturaMinEx,
                 Material, tiempo_de_prepa):

        self.marca = marca
        self.modelo = modelo
        self.tamaño = tamaño
        self.capacidad = capacidad
        self.temperaturaMaxEx = temperaturaMaxEx
        self.temperaturaMinEx = temperaturaMinEx
        self.Material = Material
        self.tiempo_de_prepa = tiempo_de_prepa


class Placa_Calefactora:  # definiendo clase de la placa calefactora
    def __init__(self, TemperaturaMax, PasodeCo, Estado):

        self.TemperaturaMax = TemperaturaMax
        self.PasodeCo = PasodeCo
        self.Estado = Estado


class Resistencia:  # definiendo clase de la resistencia
    def __init__(self, Potencia, Voltaje, Estado, Temperatura):

        self.Potencia = Potencia
        self.Voltaje = Voltaje
        self.Estado = Estado
        self.Temperatura = Temperatura


class deposito:  # definiendo clase del deposito
    def __init__(self, tamaño, capacidad):

        self.tamaño = tamaño
        self.capacidad = capacidad


class sensor:  # definiendo clase de los sensores
    def __init__(self, tipo_sensor, nivel_exactitud,
                 unidad_medida, medidas_comparacion):

        self.tipo_sensor = tipo_sensor
        self.nivel_exactitud = nivel_exactitud
        self.unidad_medida = unidad_medida
        self.medidas_comparacion = medidas_comparacion


class Filtro:  # definiendo clase del filtro
    def __init__(self, tipo, capacidad, densidad, material):

        self.tipo = tipo
        self.capacidad = capacidad
        self.densidad = densidad
        self.material = material


class goteo:  # definiendo clase de goteo
    def __init__(self, cantidadagua):

        self.cantidad = cantidadagua


class jarra:  # definiendo clase de la jarra
    def __init__(self, capacidad, nivel_lleno):

        self.capacidad = capacidad
        self.nivelleno = nivel_lleno


class indicador:  # definiendo clase indicador
    def __init__(self, tipo, estado):

        self.tipo = tipo
        self.estado = estado


# ================= DEFINICION DE OBJETOS =================

cafetera1 = Cafetera(
    "Oster",
    "BVSTEM7301",
    "34.5 cm ×27.8 cm ×30 cm",
    "2.8 litros",
    "96 °C",
    "88 °C",
    "ACERO Y PLASTICO",
    "3-4 MINUTOS"
)

Placa1 = Placa_Calefactora(
    "55° y 60°",
    "1380W - 1450W",
    "Encendido/Apagado"
)

Resis1 = Resistencia(
    "1380W - 1450W",
    "120v",
    "Encendido/Apagado",
    "88°C - 96°C"
)

deposito1 = deposito(
    "23.5cm * 22.5cm * 6cm",
    "2.8 litros"
)

sensor1 = sensor(
    "nivel de agua",
    "100%",
    "mililitros",
    "mililitros"
)

sensor2 = sensor(
    "nivel de peso",
    "85%",
    "gramos",
    "gramos"
)

filtro1 = Filtro(
    "filtro de canasta",
    "10-12 tazas",
    "8.0 g/cm³",
    "acero inoxidable"
)

jarra1 = jarra(
    "600 ml",
    "80%"
)


# ================= FUNCIONES =================

# FUNCION DE ENCENDIDO
def encendido():

    while True:

        en = input(
            "¿La cafetera está conectada a corriente? (S/N): "
        ).strip().upper()

        if en == "S":
            print("Cafetera conectada correctamente.")
            return True

        elif en == "N":
            print("Por favor conecta la cafetera.")

        else:
            print("Opción no válida")


# FUNCION PARA PEDIR NOMBRE
def pedir_nombre():

    nombre = ""

    while not nombre.strip():

        nombre = input(
            "Ingresa tu nombre de usuario: "
        ).strip()

    return nombre


# FUNCION PARA BOTON DE INICIO
def boton_inicio():

    while True:

        respuesta = input(
            "\n¿Presionó el botón de inicio? (S/N): "
        ).strip().upper()

        if respuesta == "S":

            print("Iniciando proceso...")
            return True

        elif respuesta == "N":

            print("Esperando que se presione el botón...")

        else:
            print("Opción no válida")


# FUNCION PARA COMPROBAR AGUA
def comprobar_agua(sensor_agua):

    print(f"\nSensor utilizado: {sensor_agua.tipo_sensor}")

    while True:

        respuesta = input(
            "¿El depósito tiene agua? (S/N): "
        ).strip().upper()

        if respuesta == "S":

            print("Hay agua suficiente.")
            return True

        elif respuesta == "N":

            print("No hay agua.")
            print("Agrega agua para continuar.")

        else:
            print("Opción no válida")


# FUNCION PARA LLENAR JARRA
def llenar_jarra(jarra_obj):

    while True:

        try:

            nivel = int(
                input("\nIngresa el nivel de la jarra (0 a 100): ")
            )

            if 0 <= nivel <= 100:

                jarra_obj.nivelleno = f"{nivel}%"

                print(
                    f"Nivel actualizado: {jarra_obj.nivelleno}"
                )

                return True

            else:
                print("El nivel debe estar entre 0 y 100.")

        except ValueError:

            print("Ingresa un número válido.")


# FUNCION PARA COMPROBAR POSICION DE LA JARRA
def comprobar_jarra(jarra_obj, sensor_peso):

    print(f"\nSensor utilizado: {sensor_peso.tipo_sensor}")
    print(f"Exactitud: {sensor_peso.nivel_exactitud}")

    print(f"Capacidad de la jarra: {jarra_obj.capacidad}")
    print(f"Nivel actual: {jarra_obj.nivelleno}")

    nivel = int(jarra_obj.nivelleno.replace("%", ""))

    while True:

        respuesta = input(
            "\n¿El sensor detecta la jarra colocada? (S/N): "
        ).strip().upper()

        if respuesta == "S":

            if nivel >= 90:

                print("La jarra está demasiado llena.")
                return False

            elif nivel <= 10:

                print("La jarra está muy vacía.")
                return False

            else:

                print("Jarra detectada y en nivel adecuado.")
                return True

        elif respuesta == "N":

            print(
                "El sensor no detecta la jarra."
            )

            print(
                "Colócala correctamente."
            )

        else:
            print("Opción no válida.")


# FUNCION DE VERIFICACION GENERAL
def verificacion():

    while True:

        respuesta = input(
            "\n¿Todo se verificó correctamente? (S/N): "
        ).strip().upper()

        if respuesta == "S":

            print("Se iniciará el proceso de preparación...")
            return True

        elif respuesta == "N":

            print("Entrando en modo seguro...")
            apagado_seguro()
            return False

        else:
            print("Opción no válida")


# FUNCION PARA ACTIVAR RESISTENCIA
def activar_resistencia(resistencia_obj):

    print("\nActivando resistencia...")
    print(f"Potencia: {resistencia_obj.Potencia}")
    print(f"Temperatura: {resistencia_obj.Temperatura}")


# FUNCION PARA HERVIR AGUA
def hervir_agua():

    while True:

        respuesta = input(
            "\n¿El agua ya hirvió? (S/N): "
        ).strip().upper()

        if respuesta == "S":

            print("Agua caliente lista.")
            return True

        elif respuesta == "N":

            print("Calentando agua...")

        else:
            print("Opción no válida.")


# FUNCION PARA FILTRAR CAFE
def filtrar_cafe(filtro_obj):

    print("\nFiltrando café...")
    print(f"Filtro utilizado: {filtro_obj.tipo}")
    print("Preparando café...")


# FUNCION PARA VERIFICAR SI LA JARRA ESTA LLENA
def verificar_jarra_llena(jarra_obj):

    nivel = int(jarra_obj.nivelleno.replace("%", ""))

    if nivel >= 100:

        print("\nLa jarra está completamente llena.")
        return True

    else:

        print("\nLa jarra aún no está llena.")
        return False


# FUNCION PARA ACTIVAR CALEFACTOR
def activar_calefactor(placa_obj):

    print("\nActivando calefactor...")
    print(
        f"Manteniendo temperatura entre "
        f"{placa_obj.TemperaturaMax}"
    )


# FUNCION PARA APAGAR CALEFACTOR
def apagar_calefactor():

    print("\nLa jarra fue retirada.")
    print("Apagando calefactor...")


# FUNCION DE APAGADO SEGURO
def apagado_seguro():

    print("\nEntrando en modo seguro...")
    print("Apagando sistema...")


# FUNCION PARA INICIAR CAFETERA
def iniciar_cafetera():

    print("\nLa cafetera está en funcionamiento...")
    print("Café preparado correctamente.")


# ================= FUNCION MAIN =================

def main():

    print("\n====== SISTEMA DE CAFETERA ======")

    # Verificar conexión
    encendido()

    # Pedir nombre
    nombre = pedir_nombre()

    print(f"\nHola, {nombre}! Bienvenido.")

    # Verificar botón de inicio
    boton_inicio()

    # Verificar agua
    comprobar_agua(sensor1)

    # Llenar jarra
    llenar_jarra(jarra1)

    # Verificar jarra
    if not comprobar_jarra(jarra1, sensor2):

        apagado_seguro()
        return

    # Verificación general
    if not verificacion():

        return

    # Activar resistencia
    activar_resistencia(Resis1)

    # Hervir agua
    hervir_agua()

    # Filtrar café
    filtrar_cafe(filtro1)

    # Verificar llenado de la jarra
    verificar_jarra_llena(jarra1)

    # Activar calefactor
    activar_calefactor(Placa1)

    # Verificar si la jarra sigue puesta
    respuesta = input(
        "\n¿La jarra sigue colocada? (S/N): "
    ).strip().upper()

    if respuesta == "N":

        apagar_calefactor()

    # Finalizar
    iniciar_cafetera()


# ================= EJECUCION =================

main()