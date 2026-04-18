#include <stdio.h>

int main()
{
    int cantH, cantV, cantA;
    float precioh, preciov, precioa;
    float totalH, totalV, totalA, total, totalContado;

    printf("Ingrese la cantidad de hojas de hielo seco: ");
    scanf("%d", &cantH);

    printf("Ingrese el precio unitario de las hojas de hielo seco: ");
    scanf("%f", &precioh);

    printf("Ingrese la cantidad de viguetas: ");
    scanf("%d", &cantV);

    printf("Ingrese el precio unitario de las viguetas: ");
    scanf("%f", &preciov);

    printf("Ingrese la cantidad de armazones: ");
    scanf("%d", &cantA);

    printf("Ingrese el precio unitario de los armazones: ");
    scanf("%f", &precioa);

    totalH = cantH * precioh;
    totalH = totalH - (totalH * 0.20);

    totalV = cantV * preciov;
    totalV = totalV - (totalV * 0.15); 

    totalA = cantA * precioa; 

    total = totalH + totalV + totalA;

    totalContado = total - (total * 0.07);

    printf("\nTotal a pagar si se paga a  credito: %.2f\n", total);
    printf("Totala pagar si se paga de contado (con 7%% descuento): %.2f\n", totalContado);

    return 0;
}