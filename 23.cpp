#include <stdio.h>
#include <math.h>

int main()
{
    int opcion;
    float angulo, rad;

    printf("Como esta el angulo?\n");
    printf("1. Grados\n");
    printf("2. Radianes\n");
    scanf("%d", &opcion);

    printf("Ingrese el valor del angulo: ");
    scanf("%f", &angulo);

    if(opcion == 1)
    {
        rad = angulo * 3.1416 / 180;
    }
    else if(opcion == 2)
    {
        rad = angulo;
    }
    else
    {
        printf("Opcion no valida\n");
        return 0;
    }

    float tangente = tan(rad);
    float secante = 1 / cos(rad);
    float cotangente = 1 / tan(rad);
    float cosecante = 1 / sin(rad);

    printf("\nResultados:\n");
    printf("Tangente: %.4f\n", tangente);
    printf("Secante: %.4f\n", secante);
    printf("Cotangente: %.4f\n", cotangente);
    printf("Cosecante: %.4f\n", cosecante);

    return 0;
}