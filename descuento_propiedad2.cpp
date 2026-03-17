#include <cstdio>
int main() 
{
  float Largo, Ancho, PrecioporM, Area, PrecioTotal;
  printf("---------------Sistema de Descuento version 2.0 by JEPR---------------\n");
  printf("Ingrese el largo de su propiedad -->: ");
  scanf("%f", &Largo);
  printf("Ingrese el ancho de su propiedad -->: ");
  scanf("%f", &Ancho);
  printf("Ingrese el precio por metro cuadrado -->: ");
  scanf("%f", &PrecioporM);
  Area = Largo * Ancho;
  PrecioTotal = Area * PrecioporM;
    if(Area > 1000){
       PrecioTotal = (PrecioTotal * 0.25);
       printf("Segun los datos ingresados se aplico un descuento del 25%%\n");
}
    else if(Area > 500)
    {
       PrecioTotal = (PrecioTotal * 0.17);
       printf("Segun los datos ingresados se aplico un descuento del 17%%\n");   
    }
    else if(Area > 400)
    {
       PrecioTotal = (PrecioTotal * 0.10);
       printf("Segun los datos ingresados se aplico un descuento del 10%%\n");
    }
    else
    {
       printf("Segun los datos ingresados No se aplica descuento al precio de su propiedad\n");
    }

printf("El area de la propiedad es: %.2f m2\n", Area);
printf("El precio total de la propiedad es: %.2f\n", PrecioTotal);

return 0;
}