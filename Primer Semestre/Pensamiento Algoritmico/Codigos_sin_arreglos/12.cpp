#include <stdio.h>

int main()
{
    char nombre[50];
    int tipo, horas;
    float cuota, sueldo;
    int horasExtra;
    float multiplicador;

    printf("Ingrese el nombre del empleado: ");
    scanf("%s", nombre);

    printf("Ingrese el tipo de empleado (1-4): ");
    scanf("%d", &tipo);

    printf("Ingrese las horas trabajadas: ");
    scanf("%d", &horas);

    printf("Ingrese la cuota por hora: ");
    scanf("%f", &cuota);

    switch(tipo)
    {
        case 1: multiplicador = 1.5; 
        break;
        
        case 2: multiplicador = 2.0;
        break;

        case 3: multiplicador = 2.5;
        break;

        case 4: multiplicador = 3.0;
        break;

        default:
            printf("Tipo de empleado no valido\n");
            return 0;
    }

    if(horas <= 40)
    {
        sueldo = horas * cuota;
    }
    else
    {
        horasExtra = horas - 40;
        sueldo = (40 * cuota) + (horasExtra * cuota * multiplicador);
    }

    printf("\nEmpleado: %s\n", nombre);
    printf("Sueldo a pagar: %.2f\n", sueldo);

    return 0;
}