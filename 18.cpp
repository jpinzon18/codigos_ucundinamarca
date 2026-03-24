#include <stdio.h>

int main()
{
    char nombre[50];
    float promedio;
    int tipo;

    printf("Por favor Ingrese el nombre del aspirante: ");
    scanf("%s", nombre);

    printf("Por favor Ingrese el promedio de bachillerato: ");
    scanf("%f", &promedio);

    printf("Ingrese el tipo de bachillerato (recuerde que:1-Fisico Matematico, 2-5 otros): ");
    scanf("%d", &tipo);

    if(promedio > 90 || (promedio >= 80 && promedio <= 90 && tipo == 1))
    {
        printf("Aspirante %s: debido a su promedio usted esta ACEPTADO\n", nombre);
    }
    else
    {
        printf("Aspirante %s: debido a su promedio usted esta RECHAZADO\n", nombre);
    }

    return 0;
}