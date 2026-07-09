#include <stdio.h>

int main()
{
    int x;
    int suma = 0;
   
    printf("Ingrese un numero -->: ");
    scanf("%d", &x);
   
    while (x != 0)
    {
        suma = suma + x;
        printf("La suma por el momento es -->: %d\n ", suma);
        printf("Ingrese un numero -->; ");
        scanf("%d", &x);
    }
    
    printf("El programa ha finalizado su ejecucion :).\n");
   
    return 0;
}