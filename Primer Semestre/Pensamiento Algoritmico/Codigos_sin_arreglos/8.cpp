#include <stdio.h>

int main()
{
    float A, B, C;

    printf("Ingrese el angulo A -->: ");
    scanf("%f", &A);

    printf("Ingrese el angulo B -->: ");
    scanf("%f", &B);

    printf("Ingrese el angulo C -->: ");
    scanf("%f", &C);

    if(A + B + C == 180)
    {
        if(A == 90 || B == 90 || C == 90)
        {
            printf("Segun los angulos ingresados el triangulo es Rectangulo\n");
        }
        else if(A > 90 || B > 90 || C > 90)
        {
            printf("Segun los angulos ingresados el triangulo es Obtusangulo\n");
        }
        else
        {
            printf("Segun los angulos ingresados el triangulo es Acutangulo\n");
        }
    }
    else
    {
        printf("Segun los angulos ingresados No es un triangulo valido\n");
    }

    return 0;
}