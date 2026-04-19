#include <stdio.h>

int main() 
{
    int m[6][6];
    int i, j;
    int suma;

    for (i = 0; i < 6; i++)
     {
        for (j = 0; j < 6; j++) 
        {
            printf("Ingrese elemento [%d][%d]: ", i, j);
            scanf("%d", &m[i][j]);
        }
    }

    printf("\nMATRIZ:\n");

    for (i = 0; i < 6; i++) 
    {
        for (j = 0; j < 6; j++) 
        {
            printf("%5d", m[i][j]);
        }
        printf("\n");
    }

    printf("\nSUMA POR COLUMNAS:\n");

    for (j = 0; j < 6; j++)
    {
        suma = 0;
        for (i = 0; i < 6; i++)
        {
            suma += m[i][j];
        }
        printf("%5d", suma);
    }

    printf("\n");

    return 0;
}