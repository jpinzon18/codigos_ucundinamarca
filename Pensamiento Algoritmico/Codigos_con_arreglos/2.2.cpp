#include <stdio.h>

int main() 
{
    char poblacion[50], poblacionMax[50], poblacionMin[50];
    float lluvia, lluviaMax, lluviaMin;
    int i;
    int inicializado = 0;

    for (i = 1; i <= 45; i++) 
    {
        printf("Ingrese nombre de la poblacion: ");
        scanf("%s", poblacion);

        printf("Ingrese total de lluvia: ");
        scanf("%f", &lluvia);

        if (lluvia > 0) 
        {
            if (!inicializado) 
            {
                lluviaMax = lluvia;
                lluviaMin = lluvia;
                sprintf(poblacionMax, "%s", poblacion);
                sprintf(poblacionMin, "%s", poblacion);
                inicializado = 1;
            } else 
            {
                if (lluvia > lluviaMax) 
                {
                    lluviaMax = lluvia;
                    sprintf(poblacionMax, "%s", poblacion);
                }
                if (lluvia < lluviaMin) 
                {
                    lluviaMin = lluvia;
                    sprintf(poblacionMin, "%s", poblacion);
                }
            }
        }
    }

    if (inicializado) 
    {
        printf("Poblacion con mayor lluvia: %s con %.2f\n", poblacionMax, lluviaMax);
        printf("Poblacion con menor lluvia: %s con %.2f\n", poblacionMin, lluviaMin);
    } else 
    {
        printf("No hubo registros de lluvia.\n");
    }

    return 0;
}