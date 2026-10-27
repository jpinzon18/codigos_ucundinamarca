prestamo=float(input("Por favor ingrese el valor de su prestamo -->:"))
tasint=float(input("Por favor ingrese su tasa de interes (0 a 100) -->:"))
meses=int(input("Ingrese el numero de meses que dura el prestamo -->:"))
abono=float(input("Por favor ingrese el abono que desea hacer -->:"))

saldo=prestamo
total_intereses = 0

for mes in range(1, meses + 1):
    intereses = saldo*tasint/100
    saldo = saldo+intereses
    total_intereses=total_intereses+intereses

    pago=abono

    if pago > saldo:
        pago = saldo

    saldo = saldo - pago

    print("Mes -->:",mes)
    print("Intereses -->:",round(pago, 2))
    print("Abono -->:",round(pago, 2))
    print("Saldo Pendiente -->:",round(saldo, 2))

    print("Total de intereses pagados -->:",round(total_intereses,2))

    if saldo <= 0:
        print("el prestamo fue cancelado")
    else:
        print("existe una deuda pendiente de -->: ",round(saldo, 2))