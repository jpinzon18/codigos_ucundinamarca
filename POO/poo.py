class Apple:
    procesador = "chip M4 Pro"
    RAM = "24 GB"
    SSD = "512 GB"


class Dell:
    procesador = "Intel core ultra 7"
    RAM = "32 GB"
    SSD = "1 TB"


class Asus:
    procesador = "Intel core ultra 7"
    RAM = "16 GB"
    SSD = "2 TB"


def esc():
    cantidad = int(input("Cantidad de Apple a crear: "))
    for i in range(cantidad):
        apple = Apple()
        print("\n", f"Apple{i+1}", apple.procesador, apple.RAM, apple.SSD, sep="\n")


def esc1():
    cantidad = int(input("Cantidad de Dell a crear: "))
    for i in range(cantidad):
        dell = Dell()
        print("\n", f"Dell{i+1}", dell.procesador, dell.RAM, dell.SSD, sep="\n")


def esc2():
    cantidad = int(input("Cantidad de Asus a crear: "))
    for i in range(cantidad):
        asus = Asus()
        print("\n", f"Asus{i+1}", asus.procesador, asus.RAM, asus.SSD, sep="\n")


def menu():
    while True:
        print("\nBienvenido a la fábrica de computadores")
        print("Oprime 1 para Fabricar Apple")
        print("Oprime 2 para Fabricar Dell")
        print("Oprime 3 para Fabricar Asus")
        print("Oprime 4 para Finalizar el Programa")

        e = int(input("Seleccione una opción: "))

        if e == 1:
            esc()
        elif e == 2:
            esc1()
        elif e == 3:
            esc2()
        elif e == 4:
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida, intenta de nuevo.")


menu()