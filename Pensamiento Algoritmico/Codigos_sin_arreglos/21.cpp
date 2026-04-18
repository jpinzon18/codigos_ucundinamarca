#include <stdio.h>

int main()
{
    char nombre[50];
    int TipoE;
    float sueldo, aumento, sueldof;

    printf("Por favor ingrese su nombre -->: \n");
    scanf("%s", nombre);

    printf("Por favor ingrese su tipo de empleado -->: \n");
    scanf("%d", &TipoE);

    printf("Por favor ingrese su sueldo -->: \n");
    scanf("%f", &sueldo);

    switch (TipoE)
    {
    case 1:
        aumento = sueldo * 0.05;
        break;
    case 2:
        aumento = sueldo * 0.07;
        break;
    case 3:
        aumento = sueldo * 0.09;
        break;
    case 4:
        aumento = sueldo * 0.12;
        break;
    case 5:
        aumento = sueldo * 0.15;
        break;
    default:
        printf("El Tipo de empleado que digito no es valido\n");
        return 0;
    }

    sueldof = sueldo + aumento;

    printf("Empleado: %s\n", nombre);
    printf("Su Sueldo final con aumento es: %.2f\n", sueldof);

    return 0;
}