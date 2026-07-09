Algoritmo tres_en_raya
    Definir tablero Como Caracter
    Dimension tablero[3,3]
    Definir i, j, fila, col Como Entero
    Definir jugador, ganador Como Caracter

    Para i <- 1 Hasta 3
        Para j <- 1 Hasta 3
            tablero[i,j] <- " "
        FinPara
    FinPara

    jugador <- "X"
    ganador <- " "

    Para i <- 1 Hasta 9
        Escribir "Turno del jugador ", jugador

        Para j <- 1 Hasta 3
            Escribir tablero[j,1], " | ", tablero[j,2], " | ", tablero[j,3]
            Escribir "----------"
        FinPara

        Repetir
            Escribir "Ingrese fila (1-3):"
            Leer fila
            Escribir "Ingrese columna (1-3):"
            Leer col

            Si fila < 1 O fila > 3 O col < 1 O col > 3 Entonces
                Escribir "Posicion fuera de rango. Intente nuevamente."
            Sino
                Si tablero[fila,col] <> " " Entonces
                    Escribir "Esa posicion ya esta ocupada intente nuevamente "
                FinSi
            FinSi
        Hasta Que fila >= 1 Y fila <= 3 Y col >= 1 Y col <= 3 Y tablero[fila,col] = " "

        tablero[fila,col] <- jugador

        Si tablero[1,1] = jugador Y tablero[1,2] = jugador Y tablero[1,3] = jugador Entonces
            ganador <- jugador
        FinSi
        Si tablero[2,1] = jugador Y tablero[2,2] = jugador Y tablero[2,3] = jugador Entonces
            ganador <- jugador
        FinSi
        Si tablero[3,1] = jugador Y tablero[3,2] = jugador Y tablero[3,3] = jugador Entonces
            ganador <- jugador
        FinSi
        Si tablero[1,1] = jugador Y tablero[2,1] = jugador Y tablero[3,1] = jugador Entonces
            ganador <- jugador
        FinSi
        Si tablero[1,2] = jugador Y tablero[2,2] = jugador Y tablero[3,2] = jugador Entonces
            ganador <- jugador
        FinSi
        Si tablero[1,3] = jugador Y tablero[2,3] = jugador Y tablero[3,3] = jugador Entonces
            ganador <- jugador
        FinSi
        Si tablero[1,1] = jugador Y tablero[2,2] = jugador Y tablero[3,3] = jugador Entonces
            ganador <- jugador
        FinSi
        Si tablero[1,3] = jugador Y tablero[2,2] = jugador Y tablero[3,1] = jugador Entonces
            ganador <- jugador
        FinSi

        Si ganador <> " " Entonces
            Escribir "El ganador es ", ganador
            i <- 10
        Sino
            Si i = 9 Entonces
                Escribir "Empate"
            Sino
                Si jugador = "X" Entonces
                    jugador <- "O"
                Sino
                    jugador <- "X"
                FinSi
            FinSi
        FinSi
    FinPara

    Escribir "Tablero final:"
    Para i <- 1 Hasta 3
        Escribir tablero[i,1], " | ", tablero[i,2], " | ", tablero[i,3]
        Escribir "----------"
    FinPara
FinAlgoritmo