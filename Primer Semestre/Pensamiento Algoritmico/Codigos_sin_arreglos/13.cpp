#include <stdio.h>

int main()
{
    float lado, costoA;
    float base, altura, costoB;
    float areaA, areaB, totalA, totalB;

    printf("Ingrese el lado del terreno A -->: ");
    scanf("%f", &lado);

    printf("Ingrese el costo por metro cuadrado  del terreno A -->: ");
    scanf("%f", &costoA);

    printf("Ingrese la base del terreno B -->: ");
    scanf("%f", &base);

    printf("Ingrese la altura del terreno B -->: ");
    scanf("%f", &altura);

    printf("Ingrese el costo por metro cuadrado del terreno B -->: ");
    scanf("%f", &costoB);

    areaA = lado * lado;
    totalA = areaA * costoA;

    areaB = base * altura;
    totalB = areaB * costoB;

    if(totalA < totalB)
    {
        printf("\nEl terreno A es mas barato\n");
        printf("Costo A: %.2f\n", totalA);
    }
    else if(totalB < totalA)
    {
        printf("\nEl terreno B es mas barato\n");
        printf("Costo B: %.2f\n", totalB);
    }
    else
    {
        printf("\nAmbos terrenos cuestan lo mismo\n");
        printf("Costo: %.2f\n", totalA);
    }

    return 0;
}