Type_of_tar = int(input("A continuacion por favor digite el numero de tipo de su tarjeta ->: "))
Limit_credit = float(input("Ahora por favor digite su limite de credito actual ->: "))

match Type_of_tar:
    case 1:
        more_credit = (Limit_credit*0.25)
    case 2:
        more_credit = (Limit_credit*0.35)
    case 3:
        more_credit = (Limit_credit*0.40)
    case _:
        more_credit = (Limit_credit*0.50)

New_limit = (Limit_credit + more_credit)

print(f"el aumento de su credito fue de {more_credit}")
print(f"Su nuevo limite de credito es -->: {New_limit}")
