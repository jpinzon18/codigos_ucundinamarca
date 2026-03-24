#include <stdio.h>

int main()
{
    char nombre[50];
    float cal1, cal2, cal3, Total;

    printf("Por favor ingrese su nombre: ");
    scanf("%s", nombre);

    printf("Ingrese la primera nota parcial: ");
    scanf("%f", &cal1);

    printf("Ingrese la segunda nota parcial: ");
    scanf("%f", &cal2);

    printf("Ingrese la tercera nota parcial: ");
    scanf("%f", &cal3);

    if(cal1 > 70 && cal2 > 70 && cal3 > 70)
    {
        Total = (cal1 + cal2 + cal3) / 3;
        printf("El estudiante %s\n", nombre);
        printf("Su calificacion final es: %.2f\n", Total);
    }
    else
    {
        printf("El estudiante %s\n", nombre);
        printf("No acreditado\n");
    }

    return 0;
}