Algoritmo matriz_dos_por_dos
    Definir matriz Como Entero
    Dimension matriz[2,2]
    Definir i, j Como Entero

    Para i <- 1 Hasta 2
        Para j <- 1 Hasta 2
            Escribir "Ingrese un numero para la posicion [", i, ",", j, "]:"
            Leer matriz[i,j]
        FinPara
    FinPara

    Escribir "La matriz es:"
    Para i <- 1 Hasta 2
        Para j <- 1 Hasta 2
            Escribir Sin Saltar matriz[i,j], " "
        FinPara
        Escribir ""
    FinPara

FinAlgoritmo