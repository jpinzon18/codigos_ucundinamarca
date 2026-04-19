#include <stdio.h>

int main() 
{
    float v[8][6][7];
    int s, d, dia;

    for (s = 0; s < 8; s++) 
    {
        for (d = 0; d < 6; d++) 
        {
            for (dia = 0; dia < 7; dia++) 
            {
                printf("Sucursal %d, Depto %d, Dia %d: ", s + 1, d + 1, dia + 1);
                scanf("%f", &v[s][d][dia]);
            }
        }
    }

    printf("\nREPORTE SEMANAL DE VENTAS\n");

    for (s = 0; s < 8; s++) 
    {
        printf("\n---------------- SUCURSAL %d ----------------\n", s + 1);
        printf("DEPTO\\DIA  1     2     3     4     5     6     7\n");
        printf("----------------------------------------------------\n");

        for (d = 0; d < 6; d++) 
        {
            printf("DEPTO-%d   ", d + 1);

            for (dia = 0; dia < 7; dia++) 
            {
                printf("%5.1f ", v[s][d][dia]);
            }

            printf("\n");
        }
    }

    return 0;
}