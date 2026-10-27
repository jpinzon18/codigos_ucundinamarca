#lista1 = []
#lista2 = []
#lista3 = []

#print("Carga de la primera lista")
#for i in range(4):
#    numero = int(input(f"Ingrese el elemento {i + 1} de la lista 1: "))
#    lista1.append(numero)

#print("\nCarga de la segunda lista")
#for i in range(4):
#    numero = int(input(f"Ingrese el elemento {i + 1} de la lista 2: "))
#    lista2.append(numero)


#for i in range(4):
#    lista3.append(lista1[i] + lista2[i])

#print("\nLista 1:", lista1)
#print("Lista 2:", lista2)
#print("Lista 3 (suma de las posiciones):", lista3)

numeros = []
i = 0

while i < 10:
    num = int(input("Ingrese un número entero: "))
    numeros.append(num)
    i += 1

i = 0
while i < len(numeros):
    if numeros[i] == 5:
        numeros.pop(i)
    else:
        i += 1

print("Lista después de eliminar los números 5:", numeros)