#a = 6
#b = 3
#a /= 2 * b
#print(a)

#print("+" + 10 * "-" + "+")
#print(("|" + " " * 10 + "|\n") * 5, end="")
#print("+" + 10 * "-" + "+")

#x = 1
#y = 2
#z = x
#x = y
#y = z
#print(x, y)

#x = input()
#y = input()
#print(x + y)

#x = int(input())
#y = int(input())

#x = x / y
#y = y / x

#print(y)

#x = int(input())
#y = int(input())

#x = x % y
#x = x % y
#y = y % x

#print(y)

#x = input()
#y = int(input())

#print(x * y)

#z = y = x = 1
#print(x, y, z, sep='*')

#y = 2 + 3 * 5.
#print(Y)

#x = 1 / 2 + 3 // 3 + 4 ** 2
#print(x)

#x = int(input())
#y = int(input())

#print(x + y)

#largest_number = -99999999
#counter = 0

#number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

#while number != -1:
#    if number == -1:
#        continue
#    counter += 1

#    if number > largest_number:
#        largest_number = number
#    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

#if counter:
#    print("El número más grande es", largest_number)
#else:
#    print("No has ingresado ningún número.")

#numbers = [10, 5, 7, 2, 1]
#print("Contenido de la lista original:", numbers)  # Imprimiendo contenido de la lista original.

#numbers[0] = 111
#print("\nPrevio contenido de la lista:", numbers)  # Imprimiendo contenido de la lista anterior.

#numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
#print("Nuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.

#numbers = [10, 5, 7, 2, 1]
#print("Contenido de la lista original:", numbers)  # Imprimiendo el contenido de la lista original.

#numbers[0] = 111
#print("\nContenido de la lista con cambio:", numbers)  # Imprimiendo contenido de la lista con 111.

#numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
#print("Contenido de la lista con intercambio:", numbers)  # Imprimiendo contenido de la lista con intercambio.

#print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.

# Cubo - un arreglo tridimensional (3x3x3)

#cube = [[[':(', 'x', 'x'],
#         [':)', 'x', 'x'],
#         [':(', 'x', 'x']],

#        [[':)', 'x', 'x'],
#         [':(', 'x', 'x'],
#         [':)', 'x', 'x']],

#        [[':(', 'x', 'x'],
#         [':)', 'x', 'x'],
#         [':)', 'x', 'x']]]

#print(cube)
#print(cube[0][0][0])  # output: ':('
#print(cube[2][2][0])  # output: ':)'

#x = 1
#x = x == x

#print(x)

#i = 0
#while i <= 3 :
#    i += 2
#    print("*")

#i = 0
#while i <= 5 :
#    i += 1
#    if i % 2 == 0:
#      break
#    print("*")

#for i in range(1):
#    print("#")
#else:
#    print("#")

#var = 0
#while var < 6:
#    var += 1
#    if var % 2 == 0:
#        continue
#    print("#")

#var = 0
#while var < 6:
#    var += 1
#    if var % 2 == 0:
#        continue
#    print("#")

#var = 1
#while var < 10:
#    print("#")
#    var = var << 1

#z = 10
#y = 0
#x = y < z and z > y or y > z and z < y
#print(x)

#a = 1
#b = 0
#c = a & b
#d = a | b
#e = a ^ b

#print(c + d + e)

#my_list = [3, 1, -2]
#print(my_list[my_list[-1]])

#my_list = [1, 2, 3, 4]
#print(my_list[-3:-2])
#nums = [1, 2, 3]
#vals = nums[-1:-2]

#print(vals)
#print(nums)

#my_list_1 = [1, 2, 3]
#my_list_2 = []
#for v in my_list_1:
#    my_list_2.insert(0, v)
#print(my_list_2)

#my_list = [1, 2, 3]
#for v in range(len(my_list)):
#    my_list.insert(1, my_list[v])
#print(my_list)

#t = [[3-i for i in range (3)] for j in range (3)]
#s = 0
#for i in range(3):
#    s += t[i][i]
#print(s)

#my_list = [[0, 1, 2, 3] for i in range(2)]
#print(my_list[2][0])

#def function(x=0):
#    return x

#function(1)

#def f(x):
#    if x == 0:
#        return 0
#    return x + f(x - 1)


#print(f(3))

#def fun(x):
#    x += 1
#    return x


#x = 2
#x = fun(x + 1)
#print(x)

try:
    value = input("Ingresa un valor: ")
    print(value/value)
except ValueError:
    print("Entrada incorrecta...")
except ZeroDivisionError:
    print("Entrada errónea...")
except TypeError:
    print("Entrada muy errónea...")
except:
    print("¡Buuu!")
