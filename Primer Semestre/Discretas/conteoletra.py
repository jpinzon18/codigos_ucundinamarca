# =====================================================
# IMPORTACION DE LIBRERIAS
# =====================================================

# math:
# Se usa para operaciones matematicas.
# En este programa usamos log2() para calcular
# la entropia de Shannon.

import math

# time:
# Permite agregar pausas al programa.
# Se usa para hacer la salida mas amigable visualmente.

import time


# =====================================================
# DATOS DE LA CANCION
# =====================================================

# Variables modificables con informacion de la cancion.

nombre_cancion = "Time"
artista = "Pink Floyd"
duracion = "7:02"


# =====================================================
# LETRA DE LA CANCION
# =====================================================

# La variable "cancion" es de tipo string (str).
# Un string es una cadena de texto.
#
# Python permite recorrer un string caracter por caracter.
#
# Las triple comillas permiten escribir texto en multiples lineas.

cancion = """
Ticking away the moments that make up a dull day
Fritter and waste the hours in an offhand way
Kicking around on a piece of ground in your hometown
Waiting for someone or something to show you the way

Tired of lying in the sunshine
Staying home to watch the rain
And you are young and life is long
And there is time to kill today

And then one day you find
Ten years have got behind you
No one told you when to run
You missed the starting gun

And you run and you run to catch up with the Sun
But it's sinking
Racing around to come up behind you again
The Sun is the same, in a relative way
But you're older
Shorter of breath
And one day closer to death

Every year is getting shorter
Never seem to find the time
Plans that either come to naught
Or half a page of scribbled lines (oh, oh)

Hanging on in quiet desperation
Is the English way
The time is gone, the song is over
Thought I'd something more to say

Home, home again
I like to be here when I can
And when I come home, cold and tired
It's good to warm my bones beside the fire

Far away, across the field
The tolling of the iron bell
Calls the faithful to their knees
To hear the softly spoken magic spells
"""


# =====================================================
# CONVERSION A MINUSCULAS
# =====================================================

# lower() convierte todas las letras a minusculas.
#
# Esto evita que:
# 'H' y 'h'
# se cuenten como caracteres diferentes.

cancion = cancion.lower()


# =====================================================
# EFECTOS VISUALES
# =====================================================

print("\nIniciando analisis de la cancion...")
time.sleep(1)

print("Contando caracteres...")
time.sleep(1)


# =====================================================
# DICCIONARIO DE CONTEO
# =====================================================

# "conteo" es un diccionario (dict).
#
# Un diccionario almacena:
# clave -> valor
#
# En este caso:
# caracter -> frecuencia
#
# Ejemplo:
# {
#     'a': 10,
#     'b': 3
# }

conteo = {}


# =====================================================
# RECORRER Y CONTAR CARACTERES
# =====================================================

# Este ciclo recorre la cancion caracter por caracter.
#
# Incluye:
# - letras
# - espacios
# - saltos de linea
# - simbolos

for caracter in cancion:

    # Si el caracter YA existe en el diccionario,
    # aumenta su contador en 1.

    if caracter in conteo:
        conteo[caracter] += 1

    # Si el caracter aparece por primera vez,
    # se crea dentro del diccionario con valor 1.

    else:
        conteo[caracter] = 1


print("Calculando probabilidades, porcentajes y entropia...")
time.sleep(1)


# =====================================================
# TOTAL DE CARACTERES
# =====================================================

# len() cuenta la cantidad total de caracteres
# del string.
#
# Incluye:
# - espacios
# - letras
# - saltos de linea

total_caracteres = len(cancion)


# =====================================================
# VARIABLE DE ENTROPIA
# =====================================================

# Aqui se almacenara el resultado final
# de la entropia de Shannon.

entropia = 0


# =====================================================
# ORDENAMIENTO
# =====================================================

# sorted() ordena los elementos.
#
# conteo.items() convierte el diccionario en pares:
#
# ('a', 15)
# ('b', 3)
#
# lambda x: x[1]
# significa:
# ordenar usando el segundo valor
# (la frecuencia).
#
# reverse=True:
# orden descendente.

ordenado = sorted(
    conteo.items(),
    key=lambda x: x[1],
    reverse=True
)


# =====================================================
# ENCABEZADO
# =====================================================

print("\n" + "=" * 120)
print("                    ANALISIS DE ENTROPIA DE UNA CANCION")
print("=" * 120)

print(f"Nombre   : {nombre_cancion}")
print(f"Artista  : {artista}")
print(f"Duracion : {duracion}")

print("=" * 120)


# =====================================================
# TITULOS DE TABLA
# =====================================================

# <15 significa:
# alinear a la izquierda usando 15 espacios.
#
# Esto permite que la tabla quede organizada.

print(
    f"{'CARACTER':<15}"
    f"{'FRECUENCIA':<15}"
    f"{'PROBABILIDAD':<20}"
    f"{'PORCENTAJE':<15}"
    f"{'GRAFICO'}"
)

print("-" * 120)


# =====================================================
# MOSTRAR RESULTADOS
# =====================================================

for caracter, cantidad in ordenado:

    # =================================================
    # PROBABILIDAD
    # =================================================

    # Formula:
    #
    # p(x) = frecuencia / total
    #
    # Representa la probabilidad de aparicion
    # de cada caracter.

    probabilidad = cantidad / total_caracteres


    # =================================================
    # PORCENTAJE
    # =================================================

    # Convierte la probabilidad en porcentaje.

    porcentaje = probabilidad * 100


    # =================================================
    # ENTROPIA DE SHANNON
    # =================================================

    # Formula:
    #
    # H = -Σ p(x) * log2(p(x))
    #
    # La entropia mide:
    # - cantidad de informacion
    # - incertidumbre
    # - variabilidad del texto
    #
    # Baja entropia:
    # texto repetitivo
    #
    # Alta entropia:
    # texto variado

    entropia += -probabilidad * math.log2(probabilidad)


    # =================================================
    # GRAFICO ASCII
    # =================================================

    # Repite el caracter █ tantas veces
    # como frecuencia tenga el simbolo.

    barra = "█" * cantidad


    # =================================================
    # NOMBRES LEGIBLES
    # =================================================

    # Esto mejora la visualizacion de caracteres
    # especiales.

    if caracter == " ":
        nombre = "[ESPACIO]"

    elif caracter == "\n":
        nombre = "[SALTO]"

    else:
        nombre = caracter


    # =================================================
    # MOSTRAR FILA
    # =================================================

    print(
        f"{nombre:<15}"
        f"{cantidad:<15}"
        f"{probabilidad:<20.4f}"
        f"{porcentaje:<14.2f}%"
        f"        {barra}"
    )

    # Linea vacia para separar las barras
    # y mejorar la visualizacion.

    print()

    # Pequeno retraso visual.

    time.sleep(0.05)


# =====================================================
# RESULTADOS FINALES
# =====================================================

print("-" * 120)

time.sleep(1)

print(f"TOTAL DE CARACTERES : {total_caracteres}")

time.sleep(0.5)

print(f"ENTROPIA DE SHANNON : {entropia:.4f} bits")

print("=" * 120)