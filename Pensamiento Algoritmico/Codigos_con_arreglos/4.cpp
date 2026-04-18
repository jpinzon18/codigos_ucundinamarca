#include <stdio.h>

int main()
{
    char nombre[50];
    int dias;
    float pagoDia, sueldo;

    printf("\nCALCULO DE SUELDOS (15 OBREROS)\n");

    for(int i = 0; i < 15; i++)
    {
        printf("\nNombre del obrero %d: ", i + 1);
        scanf("%s", nombre);

        printf("Cantidad de dias trabajados: ");
        scanf("%d", &dias);

        sueldo = 0;

        for(int j = 0; j < dias; j++)
        {
            printf("Pago del dia %d: ", j + 1);
            scanf("%f", &pagoDia);
            sueldo += pagoDia;
        }

        printf("Obrero: %s\n", nombre);
        printf("Sueldo total: %.2f\n", sueldo);
    }

    return 0;
}