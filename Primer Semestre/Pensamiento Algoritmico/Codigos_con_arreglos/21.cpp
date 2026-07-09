#include <stdio.h>

int main() 
{
    int m[5][4];
    int i, j;
    int esNula = 1;

    for (i = 0; i < 5; i++) 
    {
        for (j = 0; j < 4; j++) 
        {
            printf("Ingrese elemento [%d][%d]: ", i, j);
            scanf("%d", &m[i][j]);
        }
    }

    for (i = 0; i < 5; i++) 
    {
        for (j = 0; j < 4; j++) 
        {
            if (m[i][j] != 0) 
            {
                esNula = 0;
            }
        }
    }

    if (esNula == 1) 
    {
        printf("La matriz es nula\n");
    } else 
    {
        printf("La matriz no es nula\n");
    }

    return 0;
}