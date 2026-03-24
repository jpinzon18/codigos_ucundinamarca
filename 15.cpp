#include <stdio.h>

int main()
{
    int dias;
    float precio, subtotal, descuento, total;

    printf("Ingrese el numero de dias de hospedaje: ");
    scanf("%d", &dias);

    printf("Ingrese el precio por dia: ");
    scanf("%f", &precio);

    subtotal = dias * precio;

    if(dias > 15)
    {
        descuento = subtotal * 0.20;
    }
    else if(dias > 10)
    {
        descuento = subtotal * 0.15;
    }
    else if(dias > 5)
    {
        descuento = subtotal * 0.10;
    }
    else
    {
        descuento = 0;
    }

    total = subtotal - descuento;

    printf("\nSubtotal: %.2f\n", subtotal);
    printf("Descuento: %.2f\n", descuento);
    printf("Total a pagar: %.2f\n", total);

    return 0;
}