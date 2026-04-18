#include <stdio.h>

int main() 
{
    char tablero[3][3];
    int i, j, fila, col;
    char jugador = 'X';
    char ganador = ' ';

    for (i = 0; i < 3; i++) 
    {
        for (j = 0; j < 3; j++) 
        {
            tablero[i][j] = ' ';
        }
    }

    for (i = 0; i < 9; i++) 
    {
        printf("Turno del jugador %c\n", jugador);

        for (j = 0; j < 3; j++) 
        {
            printf("%c | %c | %c\n", tablero[j][0], tablero[j][1], tablero[j][2]);
            printf("----------\n");
        }

        do 
        {
            printf("Ingrese fila (1-3): ");
            scanf("%d", &fila);
            printf("Ingrese columna (1-3): ");
            scanf("%d", &col);

            if (fila < 1 || fila > 3 || col < 1 || col > 3) 
            {
                printf("Posicion fuera de rango. Intente nuevamente.\n");
            } 
            else if (tablero[fila - 1][col - 1] != ' ') 
            {
                printf("Esa posicion ya esta ocupada. Intente nuevamente.\n");
            }

        } 
        while (fila < 1 || fila > 3 || col < 1 || col > 3 || tablero[fila - 1][col - 1] != ' ');

        tablero[fila - 1][col - 1] = jugador;

        if (tablero[0][0] == jugador && tablero[0][1] == jugador && tablero[0][2] == jugador) ganador = jugador;
        if (tablero[1][0] == jugador && tablero[1][1] == jugador && tablero[1][2] == jugador) ganador = jugador;
        if (tablero[2][0] == jugador && tablero[2][1] == jugador && tablero[2][2] == jugador) ganador = jugador;

        if (tablero[0][0] == jugador && tablero[1][0] == jugador && tablero[2][0] == jugador) ganador = jugador;
        if (tablero[0][1] == jugador && tablero[1][1] == jugador && tablero[2][1] == jugador) ganador = jugador;
        if (tablero[0][2] == jugador && tablero[1][2] == jugador && tablero[2][2] == jugador) ganador = jugador;

        if (tablero[0][0] == jugador && tablero[1][1] == jugador && tablero[2][2] == jugador) ganador = jugador;
        if (tablero[0][2] == jugador && tablero[1][1] == jugador && tablero[2][0] == jugador) ganador = jugador;

        if (ganador != ' ') 
        {
            printf("El ganador es %c\n", ganador);
            break;
        } 
        else if (i == 8) 
        {
            printf("Empate\n");
        } 
        else 
        {
            if (jugador == 'X') 
            {
                jugador = 'O';
            } 
            else 
            {
                jugador = 'X';
            }
        }
    }

    printf("Tablero final:\n");
    for (i = 0; i < 3; i++) 
    {
        printf("%c | %c | %c\n", tablero[i][0], tablero[i][1], tablero[i][2]);
        printf("----------\n");
    }

    return 0;
}