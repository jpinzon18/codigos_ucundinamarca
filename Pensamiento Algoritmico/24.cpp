#include <stdio.h>

int main()
{
    float a, b, c, d, mayor;

    printf("Ingrese 4 numeros:\n");
    scanf("%f %f %f %f", &a, &b, &c, &d);

    if(a == b || a == c || a == d ||
       b == c || b == d ||
       c == d)
    {
        printf("Error: hay numeros iguales\n");
    }
    else
    {
        mayor = a;

        if(b > mayor) mayor = b;
        if(c > mayor) mayor = c;
        if(d > mayor) mayor = d;

        printf("El numero mayor es: %.2f\n", mayor);
    }

    return 0;
}