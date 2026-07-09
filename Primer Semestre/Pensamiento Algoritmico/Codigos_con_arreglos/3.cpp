#include <stdio.h>

int main()
{
    char nombre[50];
    int dias;
    float pagoDia, sueldo;
    char continuar;

    do
    {
        printf("\nNombre del obrero: ");
        scanf("%s", nombre);

        printf("Cantidad de dias trabajados: ");
        scanf("%d", &dias);

        sueldo = 0;

        for(int i = 0; i < dias; i++)
        {
            printf("Pago del dia %d: ", i + 1);
            scanf("%f", &pagoDia);
            sueldo += pagoDia;
        }

        printf("Obrero: %s\n", nombre);
        printf("Sueldo total: %.2f\n", sueldo);

        printf("\nDesea ingresar otro obrero? (s/n): ");
        scanf(" %c", &continuar);

    } while(continuar == 's' || continuar == 'S');

    return 0;
}