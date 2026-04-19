#include <stdio.h>

int main() 
{
    int obreros, i, j;
    char nombre[50];

    int prodDia;
    int suma, diasArriba;
    float promedio;

    int totalProdMes = 0;
    float totalProm = 0;
    int totalDiasArriba = 0;

    printf("Ingrese cantidad de obreros: ");
    scanf("%d", &obreros);

    printf("\nMENSUAL DE PRODUCCION\n");
    printf("NOMBRE                PROD.MES  PROM.DIA  DIAS ARRIBA\n");
    printf("------------------------------------------------------\n");

    for (i = 1; i <= obreros; i++) 
    {
        suma = 0;
        diasArriba = 0;

        printf("Ingrese nombre del obrero: ");
        scanf("%s", nombre);

        for (j = 1; j <= 30; j++) 
        {
            printf("Produccion dia %d: ", j);
            scanf("%d", &prodDia);
            suma += prodDia;
        }

        promedio = suma / 30.0;

        for (j = 1; j <= 30; j++) 
        {
            printf("Reingrese produccion dia %d para calcular dias arriba: ", j);
            scanf("%d", &prodDia);
            if (prodDia > promedio) 
            {
                diasArriba++;
            }
        }

        printf("%-20s %8d %9.2f %10d\n", nombre, suma, promedio, diasArriba);

        totalProdMes += suma;
        totalProm += promedio;
        totalDiasArriba += diasArriba;
    }

    printf("------------------------------------------------------\n");
    printf("TOTAL                %8d %9.2f %10d\n",
           totalProdMes, totalProm, totalDiasArriba);

    return 0;
}