points=int(input("Por favor digite el numero de puntos que obtuvo su equipo -->: "))

match points:
    case n if points <= 20:
        print("Su equipo esta en zona de Descenso")
    case n if points <= 40:
        print("Su equipo esta en un nivel intermedio")
    case n if points <= 60:
        print("Su equipo esta siendo competitivo en la liga")
    case n if points <= 80:
        print("Su equipo es Destacado en la liga")
    case n if points <= 100:
        print("Su equipo ha sido campeon de liga")

