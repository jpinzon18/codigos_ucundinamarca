#include <stdio.h>

int main()
{
    float A1, B1, C1, L1a, L1b, L1c;
    float A2, B2, C2, L2a, L2b, L2c;

    printf("Datos del Triangulo 1\n");
    printf("Por favor Ingrese los angulos: ");
    scanf("%f %f %f", &A1, &B1, &C1);

    printf("Por favor Ingrese los lados: ");
    scanf("%f %f %f", &L1a, &L1b, &L1c);

    printf("\nDatos del Triangulo 2\n");
    printf(" Por favor Ingrese los angulos: ");
    scanf("%f %f %f", &A2, &B2, &C2);

    printf("Por favor Ingrese los lados: ");
    scanf("%f %f %f", &L2a, &L2b, &L2c);

    if(A1 == A2 && B1 == B2 && C1 == C2 &&
       L1a == L2a && L1b == L2b && L1c == L2c)
    {
        printf("\nLos triangulos son congruentes\n");
    }
    else
    {
        printf("\nLos triangulos no son congruentes\n");
    }

    return 0;
}