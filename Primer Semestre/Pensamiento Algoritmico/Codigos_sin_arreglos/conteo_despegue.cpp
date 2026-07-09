#include <stdio.h>
#include <thread>

int main()
{
    int a;
    int b;
    b=0;
    printf("Escriba un numero menor a 5 -->: ");
    scanf("%d", &a);
   
    for (a=a+1; a<=10; a++)
    {
        printf("El conteo va en  -->: %d segundos \n" ,a);
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }
    std::this_thread::sleep_for(std::chrono::seconds(1));
    printf("----------------------!DESPEGUE¡------------------------------- \n");
    std::this_thread::sleep_for(std::chrono::seconds(1));
    for (b=b+1; b<=10; b++)
    {
        printf("El conteo post-lanzamiento va en -->: %d segundos \n" ,b);
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }
    std::this_thread::sleep_for(std::chrono::seconds(1));
    printf("--------------------FINAL DEL PROGRAMA-------------------------");
    return 0;
}