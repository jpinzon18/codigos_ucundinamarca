#include <stdio.h>

int main() 
{
    float v[8][6][4][7];
    int s, d, ven, dia;

    for (s = 0; s < 8; s++) 
    {
        for (d = 0; d < 6; d++) 
        {
            for (ven = 0; ven < 4; ven++) 
            {
                for (dia = 0; dia < 7; dia++) 
                {
                    printf("Sucursal %d, Depto %d, Vendedor %d, Dia %d: ",
                           s + 1, d + 1, ven + 1, dia + 1);
                    scanf("%f", &v[s][d][ven][dia]);
                }
            }
        }
    }

    printf("\nREPORTE SEMANAL DE VENTAS\n");

    for (s = 0; s < 8; s++) 
    {
        printf("\n================ SUCURSAL %d ================\n", s + 1);

        for (d = 0; d < 6; d++) 
        {
            printf("\n------------- DEPARTAMENTO %d -------------\n", d + 1);
            printf("D1    D2    D3    D4    D5    D6    D7\n");
            printf("----------------------------------------\n");

            for (ven = 0; ven < 4; ven++) 
            {
                printf("VEN-%d ", ven + 1);

                for (dia = 0; dia < 7; dia++) 
                {
                    printf("%5.1f ", v[s][d][ven][dia]);
                }

                printf("\n");
            }
        }
    }

    return 0;
}