#include <stdio.h>

int main()
{
  float a,b,c,d,e,f,x,y;

  printf("Por favor digite el coeficiente a -->:");
  scanf("%f", &a);

  printf("Por favor digite el coeficiente b -->:");
  scanf("%f", &b);

  printf("Por favor digite el coeficiente c -->:");
  scanf("%f", &c);

  printf("Por favor digite el coeficiente d -->:");
  scanf("%f", &d);

  printf("Por favor digite el coeficiente e -->:");
  scanf("%f", &e);

  printf("Por favor digite el coeficiente f -->:");
  scanf("%f", &f);

  if((a*e - b*d) != 0)
  {
    x=(c*e - b*f)/(a*e - b*d);
    y=(a*f - c*d)/(a*e - b*d);

    printf("El valor de x es -->: %.2f \n",x);
    printf("El valor de y es -->: %.2f \n",y);
  }
  else
  {
    printf("El sistema de ecuaciones no tiene solucion\n");
  }

  return 0;
}