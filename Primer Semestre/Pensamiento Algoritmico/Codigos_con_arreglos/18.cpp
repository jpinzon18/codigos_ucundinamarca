#include <stdio.h>

int main() 
{
    int m[10][10];
    int i, j;

    for (i = 0; i < 10; i++) 
    {
        for (j = 0; j < 10; j++) 
        {
            if (i <= j) 
            {
                m[i][j] = 0;
            } else 
            {
                m[i][j] = 1;
            }
        }
    }

    printf("MATRIZ 10x10:\n");

    for (i = 0; i < 10; i++) 
    {
        for (j = 0; j < 10; j++) 
        {
            printf("%2d ", m[i][j]);
        }
        printf("\n");
    }

    return 0;
}