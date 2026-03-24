#include <stdio.h>
int main()
{
  int numeroMes;

  printf("digite el numero de mes -->: ");
  scanf("%d", &numeroMes);

  switch (numeroMes)
  {
  case 1:
    printf("El numero de mes 1 corresponde a Enero");
    break;
  case 2:
    printf("El numero de mes 2 corresponde a Febrero");
    break;
  case 3:
    printf("El numero de mes 3 corresponde a Marzo");
    break;
  case 4:
    printf("El numero de mes 4 corresponde a Abril");
    break;
  case 5:
    printf("El numero de mes 5 corresponde a Mayo");
    break;
  case 6:
    printf("El numero de mes 6 corresponde a Junio");
    break;
  case 7:
    printf("El numero de mes 7 corresponde a Julio");
    break;
  case 8:
    printf("El numero de mes 8 corresponde a Agosto");
    break;
  case 9:
    printf("El numero de mes 9 corresponde a Septiembre");
    break;
  case 10:
    printf("El numero de mes 10 corresponde a Octubre");
    break;
  case 11:
    printf("El numero de mes 11 corresponde a Noviembre");
    break;
  case 12:
    printf("El numero de mes 12 corresponde a Diciembre");
    break;
  default:
    printf("El numero que ingreso no corresponde a un numero de mes");
    break;
  }

}