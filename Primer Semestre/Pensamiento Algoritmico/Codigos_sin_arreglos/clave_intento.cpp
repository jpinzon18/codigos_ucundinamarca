#include <stdio.h>

int main()
{
    char nombre[10];
    int clave;
    int intento = 0;

    printf("Por favor digite su usuario (no mayor a 10 caracteres) -->: ");
    scanf("%s", nombre);
    printf("Hola : %s\n",nombre);

    do
    {
        printf("Por favor digite su clave de acceso -->: ");
        scanf("%d", &clave);

        if (clave != 1234) {
            intento++;
            printf("Clave incorrecta, le quedan %d intentos\n", 3 - intento);
        }

    } while (clave != 1234 && intento < 3);

    if (clave == 1234)
        printf("Bienvenido %s\nAhora puedes acceder a las funciones de tu cuenta libremente", nombre);
    else
        printf("Ha superado el limite de intentos, acceso denegado :(\n");

    return 0;
}