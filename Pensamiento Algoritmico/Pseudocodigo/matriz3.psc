Algoritmo matriz_3x3
    Definir tablero Como Entero
    Dimension tablero[3,3]
    Definir i, j Como Entero

    // Llenar la matriz (3 filas x 3 columnas)
    Para i <- 1 Hasta 3
        Para j <- 1 Hasta 3
            Escribir "Ingrese valor para [", i, ",", j, "]:"
            Leer tablero[i,j]
        FinPara
    FinPara

    // Mostrar la matriz
    Escribir "Matriz 3x3:"
    Para i <- 1 Hasta 3
        Para j <- 1 Hasta 3
            Escribir Sin Saltar tablero[i,j], " "
        FinPara
        Escribir "" // salto de línea por cada fila
    FinPara
FinAlgoritmo
