#include <stdio.h>

int main()
{
    char nombre[50];
    int partidos;
    int puntos, totalPuntos;

    printf("\nREPORTE DE JUGADORES\n");

    for(int i = 0; i < 12; i++)
    {
        printf("\nNombre del jugador %d: ", i + 1);
        scanf("%s", nombre);

        printf("Cantidad de partidos donde anoto: ");
        scanf("%d", &partidos);

        totalPuntos = 0;

        for(int j = 0; j < partidos; j++)
        {
            printf("Puntos en el partido %d: ", j + 1);
            scanf("%d", &puntos);
            totalPuntos += puntos;
        }

        printf("Jugador: %s\n", nombre);
        printf("Total de puntos: %d\n", totalPuntos);
    }

    return 0;
}