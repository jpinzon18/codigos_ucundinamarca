#include <stdio.h>

int main()
{
    char nombre[50];
    int jugadores, partidos;
    int puntos, totalPuntos;

    printf("Ingrese la cantidad de jugadores: ");
    scanf("%d", &jugadores);

    printf("\nREPORTE DE PUNTOS\n");

    for(int i = 0; i < jugadores; i++)
    {
        printf("\nNombre del jugador: ");
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