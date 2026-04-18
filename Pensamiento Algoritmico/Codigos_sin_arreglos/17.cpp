#include <stdio.h>
#include <math.h>

int main()
{
    int opcion;
    float angulo, rad;
    float sh, ch, th;

    printf("Seleccione el tipo de angulo:\n");
    printf("1. Grados\n");
    printf("2. Radianes\n");
    scanf("%d", &opcion);

    printf("Ingrese el valor del angulo: ");
    scanf("%f", &angulo);

    if(opcion == 1)
    {
        rad = angulo * M_PI / 180; 
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

    sh = sinh(rad);
    ch = cosh(rad);
    th = tanh(rad);

    printf("\nResultados:\n");
    printf("El Seno hiperbolico es: %.4f\n", sh);
    printf("El Coseno hiperbolico es: %.4f\n", ch);
    printf("El Tangente hiperbolica es: %.4f\n", th);

    return 0;
}