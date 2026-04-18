#include <stdio.h>

int main()
{
    int unidadesMaterial[6] = {3, 4, 1, 2, 3, 2};
    float costoMaterial[6];
    int totalMaterial[6] = {0,0,0,0,0,0};

    int pedido;
    char continuar;
    float costoEstimado, costoTotal = 0;

    for(int i = 0; i < 6; i++)
    {
        printf("Costo del material %d: ", i + 1);
        scanf("%f", &costoMaterial[i]);
    }

    do
    {
        printf("Cantidad de unidades del producto A: ");
        scanf("%d", &pedido);

        for(int i = 0; i < 6; i++)
        {
            totalMaterial[i] += pedido * unidadesMaterial[i];
        }

        printf("¿Otro pedido? (s/n): ");
        scanf(" %c", &continuar);

    } while(continuar == 's' || continuar == 'S');

    printf("\nLISTADO DE MATERIALES REQUERIDOS\n");
    printf("MATERIAL\tUNIDADES\tCOSTO\n");

    for(int i = 0; i < 6; i++)
    {
        costoEstimado = totalMaterial[i] * costoMaterial[i];
        printf("%d\t\t%d\t\t%.2f\n", i + 1, totalMaterial[i], costoEstimado);
        costoTotal += costoEstimado;
    }

    printf("\nCOSTO TOTAL: %.2f\n", costoTotal);

    return 0;
}