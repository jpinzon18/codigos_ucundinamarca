#include <stdio.h>
#include <string.h>

int main()
{
    char nombre[50];
    char nombreMayor[50], nombreMenor[50];

    int autos;
    float precio, totalVentas, sueldo;
    float mayorVenta = -1, menorVenta = 999999999;
    float totalGeneral = 0;

    printf("\nNOMINA QUINCENAL\n");

    for(int i = 0; i < 20; i++)
    {
        printf("\nNombre del vendedor: ");
        scanf("%s", nombre);

        printf("Cantidad de autos vendidos: ");
        scanf("%d", &autos);

        totalVentas = 0;

        for(int j = 0; j < autos; j++)
        {
            printf("Precio del auto %d: ", j + 1);
            scanf("%f", &precio);
            totalVentas += precio;
        }

        sueldo = 100 + (autos * 100) + (totalVentas * 0.02);

        printf("Vendedor: %s\n", nombre);
        printf("Total ventas: %.2f\n", totalVentas);
        printf("Sueldo: %.2f\n", sueldo);

        totalGeneral += sueldo;

        if(totalVentas > mayorVenta)
        {
            mayorVenta = totalVentas;
            strcpy(nombreMayor, nombre);
        }

        if(totalVentas < menorVenta)
        {
            menorVenta = totalVentas;
            strcpy(nombreMenor, nombre);
        }
    }

    printf("\nTOTAL GENERAL: %.2f\n", totalGeneral);

    printf("\nMayor venta:\n");
    printf("%s con %.2f\n", nombreMayor, mayorVenta);

    printf("\nMenor venta:\n");
    printf("%s con %.2f\n", nombreMenor, menorVenta);

    return 0;
}