import time
saldo = 500000

print("----Bienvendio al cajero automatico sencillo-----")
time.sleep(3)
print("oprima 1 para consultar su saldo ")
print("oprima 2 para retirar dinero en efectivo")
print("oprima 3 para consignar dinero")
print("oprima 4 para salir del programa")

time.sleep(2)
opcion=int(input("Escriba la opcion que desea usar -->: "))

match opcion:
    case 1:
        print(f"Su saldo actual es: ${saldo}")
    case 2:
        retiro = int(input("Ingrese el valor que desea retirar: "))
        if retiro <= saldo:
            saldo -= retiro
            print(f"Retiro exitoso su nuevo saldo es: ${saldo}")
        else:
            print("fondos insuficientes")
    case 3:
        consignacion =int(input("ingrese el valor a consignar -->: "))
        saldo += consignacion
        print(f"consignacion exitosa su nuevo saldo es: ${saldo}")
    case 4:
        time.sleep(1)
        print("..............Saliendo..........................")
        time.sleep(1)
        print("Gracias por usar el cajero que tenga buen dia.")
    case _:
        print("Opcion no valida")
