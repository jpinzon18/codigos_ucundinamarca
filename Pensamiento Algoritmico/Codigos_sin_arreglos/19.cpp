#include <stdio.h>
#include <string.h>

int main()
{
    char marca[50], origen[20];
    float costo, impuesto, precioVenta;

    printf("Ingrese la marca del automovil: ");
    scanf("%s", marca);

    printf("Ingrese el origen (Alemania, Japon, Italia, USA): ");
    scanf("%s", origen);

    printf("Ingrese el costo del automovil: ");
    scanf("%f", &costo);
    
    if(strcmp(origen, "Alemania") == 0)
    {
        impuesto = costo * 0.20;
    }
    else if(strcmp(origen, "Japon") == 0)
    {
        impuesto = costo * 0.30;
    }
    else if(strcmp(origen, "Italia") == 0)
    {
        impuesto = costo * 0.15;
    }
    else if(strcmp(origen, "USA") == 0)
    {
        impuesto = costo * 0.08;
    }
    else
    {
        printf("Origen no valido\n");
        return 0;
    }

    precioVenta = costo + impuesto;

    printf("\nMarca: %s\n", marca);
    printf("Impuesto: %.2f\n", impuesto);
    printf("Precio de venta: %.2f\n", precioVenta);

    return 0;
}