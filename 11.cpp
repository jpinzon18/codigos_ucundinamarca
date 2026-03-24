#include <stdio.h>

int main()
{
    float A, B;

    printf("Por favor Ingrese el angulo A: ");
    scanf("%f", &A);

    printf("Por favor Ingrese el angulo B: ");
    scanf("%f", &B);

    if(A == B)
    {
        printf("Segun los Angulos digitados El trapecio es isosceles\n");
    }
    else
    {
        printf("Segun los Angulos digitados El trapecio NO es isosceles\n");
    }

    return 0;
}