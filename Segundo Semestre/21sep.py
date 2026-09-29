#NOTA los siguientes codigos o apuntes fueron escritos el 21 de septiembre de 2026 por JEPR
def capitalism():
    sueldo=int(input("por favor ingrese su sueldo actual: "))
    if sueldo > 3000:
        print("usted debe abonar impuestos")
    else:
        print("su sueldo es menor a 3000 no debe abonar impuestos")

#capitalism()

def comparation():
    num1=int(input("ingrese el primer numero a ser comparado ->:"))
    num2=int(input("ingrese el segundo numero a ser comparado ->: "))

    if num1 > num2:
        print("el numero 1 es mayor a numero 2")
    elif num2 > num2:
        print("el numero 2 es mayor al numero 1")
    else:
        print("los numeros son iguales o no comparables")

#comparation()

def AILIKE():
    q = str(input("¿cual crees que sera mi color favorito? -->:"))

    if q == "rojo" or "ROJO":
        print("Acertaste mi color favorito efectivamente es el rojo")
    else:
        print("Lamentablemente frallaste mi color favorito es el rojo")

#AILIKE()

#if b != 0:
#    c = a/b
#    print("dentro if")
#print("fuera del if")

def elifelse():
 x = 5
 if x == 5:
     print("Es 5")
 elif x == 6:
     print("es 6")
 elif x == 7:
     print(" es 7")
 else:
     print("es otro numero")

#elifelse()

def maybe_future():
    nota = float(input("ingresa tu nota (0 a 5) ->:"))

    if nota >= 3.0:
        if nota >= 4.5:
            print("excelente")
        elif nota >= 4.0:
            print("muy bien")
        else:
            print("aprobado")
    else:
        if nota >= 2.0:
            print("reprobado debes mejorar")
        else:
            print("reprobado y ademas con bajo desempeño")

#maybe_future()

def prom():
    nota1=float(input("ingresa la primera nota ->: "))
    nota2=float(input("ingresa la segunda nota ->: "))
    nota3=float(input("ingresa la tercera nota ->: "))
    promedy=(nota1 + nota2 + nota3)/3

    if promedy >= 7:
        if promedy >= 4:
            print("regular")
        else:
            print("reprobado")
    else:
        print("Promocionado")

prom()

def bank():
    monto = float(input("ingrese su monto actual de su cuenta ->: "))
    retiro = float(input("ingrese el monto que desea retirar ->: "))

    if monto > retiro:
        print(" se puede ralizar su transaccion")
        if monto % 10 == 0:
            print("transaccion realizada correctamente")
            print("saldo actual: ",monto-retiro)
        else:
            print("su transaccion no se puede realizar debe ser multiplo de 10")
    elif retiro > monto:
        print("su transaccion no puede ser realizada debido a que el monto" \
        " de su retiro es mayor al monto disponible en su cuenta actualmente.")

#bank()