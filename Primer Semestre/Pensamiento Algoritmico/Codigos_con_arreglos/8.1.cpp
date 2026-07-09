#include <stdio.h>

int main() 
{
    int a[25];
    int i;
    int cero = 0, negativos = 0, positivos = 0;

    for (i = 0; i < 25; i++) 
    {
        printf("Ingrese numero %d: ", i + 1);
        scanf("%d", &a[i]);
    }

    printf("\nARREGLO:\n");

    for (i = 0; i < 25; i++) 
    {
        printf("%d ", a[i]);

        if (a[i] == 0) 
        {
            cero++;
        } else if (a[i] < 0) 
        {
            negativos++;
        } else 
        {
            positivos++;
        }
    }

    printf("\n\nCantidad de ceros: %d\n", cero);
    printf("Cantidad de negativos: %d\n", negativos);
    printf("Cantidad de positivos: %d\n", positivos);

    return 0;
}