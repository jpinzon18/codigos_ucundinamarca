#include <cstdio>
int main()
{
  char descripcion[50];
  float Cantidad, PrecioU, PrecioF;

  printf("---------------Descuento Precio unitario version 1.0 by JEPR---------------\n");

  printf("Ingrese la descripcion del producto -->: ");
  scanf("%s", descripcion);

  printf("Ingrese la cantidad del producto -->: ");
  scanf("%f", &Cantidad);

  printf("Ingrese el precio unitario -->: ");
  scanf("%f", &PrecioU);

  PrecioF = Cantidad * PrecioU;
  if(Cantidad > 50)
  {
    PrecioF = (PrecioF * 0.15);
  }

  printf("Segun la cantidad digitada el precio final es -->: %.2f\n", PrecioF);

  return 0;
}