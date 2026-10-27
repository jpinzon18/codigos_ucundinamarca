#Apuntes hechos el 26 de octubre de 2026 por JEPR
#for i in range(10,-1,-2):
#    print("Valor actual de i:",i)

#for i in range(5, 25, 5):
#    print("Valor actual de i: ",i)

#for i in range(1, 10, 2):
#    print("Valor actual de i:",i)

#for numero in range(5, 10):
#    print("Numero:",numero)

#for numero in range(2, 10):
#    print("Numero:",numero)

#for numero in range(10, 1, -1):
#    print("Numero:",numero)

#for numero in range(4):
#    print("Numero:",numero)

#for numero in range(10, 0, -2):
#    print("Numero:", numero)

#suma = 0
#numero = float(input("Ingrese un numero (0 para salir): "))

#while numero != 0:
#    suma += numero
#    numero = float(input("Ingrese otro numero (0 para salir): "))

#print("la suma total es: ",suma)

suma=0
contador=0

while True:
    nota=float(input("Ingrese una nota (0 -1 para terminar): "))
    if nota == -1:
        break
    suma += nota
    contador += 1

if contador > 0:
    promedio=suma/contador
    print(f"Promedio de Notas: {promedio: .2f}")
else:
    print("No se ingresaron Notas.")