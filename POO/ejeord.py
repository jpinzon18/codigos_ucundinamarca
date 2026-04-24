class Apple:
    procesador = "chip M4 Pro"
    RAM = "24 GB"
    SSD = "512 GB"
   
class DELL:
    procesador = "Intel core ultra 7"
    RAM = "32 GB"
    SSD = "1 TB"

class ASUS:
    procesador = "Intel core ultra 7"
    RAM = "16 GB"
    SSD = "2 TB"

#apple1 = Apple
#apple2 = Apple
#apple3 = Apple
#print("\n","Apple1", apple1.procesador, apple1.RAM, apple1.SSD, sep="\n")
#print("\n","Apple2", apple2.procesador, apple2.RAM, apple2.SSD, sep="\n")
#print("\n","Apple3", apple3.procesador, apple3.RAM, apple3.SSD, sep="\n")

def esc():
    cantidad = int(input("Por favor escriba la cantidad de objetos a crear: "))

    for i in range(cantidad):
        apple = Apple()  # aquí se crea la instancia
        print("\n", f"Apple{i+1}", apple.procesador, apple.RAM, apple.SSD, sep="\n")
       
def esc1():
    cantidad = int(input("Por favor escriba la cantidad de objetos a crear: "))

    for i in range(cantidad):
        dell = DELL()  # aquí se crea la instancia
        print("\n", f"Dell{i+1}", dell.procesador, dell.RAM, dell.SSD, sep="\n")

def esc2():
    cantidad = int(input("Por favor escriba la cantidad de objetos a crear: "))

    for i in range(cantidad):
        asus = ASUS()  # aquí se crea la instancia
        print("\n", f"Asus{i+1}", asus.procesador, asus.RAM, asus.SSD, sep="\n")

def menu():
    e=0
    print("bienvenido a la fabrica de computadores")
    print("Por favor oprime 1 si deseas fabricar Apple")
    print("Por favor oprime 2 si deseas fabricar Dell")
    print("Por favor oprime 3 si deseas fabricar Apple")
    print("Por favor oprime 4 si deseas finalizar el programa")
   
    if e == 1:
        esc()
    elif e == 2:
        esc1()
    if e == 3:
        esc2()
    else:
        menu()

menu()
