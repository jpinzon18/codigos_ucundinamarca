#include <stdio.h>

int main()
{
    int opcion;
    float temp, C, F, K, R;

    printf("Digite el numero segun el tipo de temperatura:\n");
    printf("1. Fahrenheit\n");
    printf("2. Celsius\n");
    printf("3. Kelvin\n");
    printf("4. Rankine\n");
    scanf("%d", &opcion);

    printf("Ingrese la temperatura que desea convertir: ");
    scanf("%f", &temp);

    switch(opcion)
    {
        case 1: 
            F = temp;
            C = (F - 32) * 5/9;
            K = C + 273;
            R = F + 460;
            break;

        case 2: 
            C = temp;
            F = (C * 9/5) + 32;
            K = C + 273;
            R = F + 460;
            break;

        case 3: 
            K = temp;
            C = K - 273;
            F = (C * 9/5) + 32;
            R = F + 460;
            break;

        case 4: 
            R = temp;
            F = R - 460;
            C = (F - 32) * 5/9;
            K = C + 273;
            break;

        default:
            printf("La Opcion digitada no es valida\n");
            return 0;
    }

    printf("\nResultados de la conversion :\n");
    printf("---------------\n");
    printf("Celsius: %.2f\n", C);
    printf("---------------\n");
    printf("Fahrenheit: %.2f\n", F);
    printf("---------------\n");
    printf("Kelvin: %.2f\n", K);
    printf("---------------\n");
    printf("Rankine: %.2f\n", R);
    printf("---------------\n");

    return 0;
}