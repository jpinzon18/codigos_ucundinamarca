#include <cstdio>
int main()
{
float X, Y;

printf("---------------Valor de X version 1.0 by JEPR---------------\n");

printf("Ingrese el Valor de X -->: ");
scanf("%f", &X);

  if(X < 0)
  {
    Y = 3*X + 6;
  }
  else
  {
    Y = X*X + 6;
  }
                 
printf("Segun los datos ingresados el valor de X es --> %.2f\n", X);
printf("Segun los datos ingresados el valor de Y es --> %.2f\n", Y);

return 0;

}