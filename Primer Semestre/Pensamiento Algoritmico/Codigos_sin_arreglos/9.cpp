#include <stdio.h>

int main()
{
    int cantidad;
    float precio, total, descuento, precioFinal;

    printf("Por favor Digite la cantidad de trajes -->: ");
    scanf("%d", &cantidad);

    printf("Por favor Digite el precio de cada traje -->: ");
    scanf("%f", &precio);

    total = cantidad * precio;

    if(cantidad == 2)
    {
        descuento = total * 0.55;
        printf("Ha hecho la Compra de 2 trajes\n");
    }
    else if(cantidad == 3)
    {
        descuento = total * 0.60;
        printf("Ha hecho la Compra de 3 trajes\n");
    }
    else if(cantidad > 3)
    {
        descuento = total * 0.65;
        printf("Ha hecho la Compra de mas de 3 trajes\n");
    }
    else
    {
        descuento = 0;
        printf("No se aplica descuento\n");
    }

    precioFinal = total - descuento;

    printf("Descuento: %.2f\n", descuento);
    printf("Precio final: %.2f\n", precioFinal);

    return 0;
}