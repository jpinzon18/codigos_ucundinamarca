#include <iostream>
using namespace std;

int main() 
{
    string nombre, nombreMax, nombreMin;
    double venta, ventaMax, ventaMin;

    for (int i = 1; i <= 20; i++) 
    {
        cout << "Ingrese nombre del vendedor: ";
        cin >> nombre;

        cout << "Ingrese total de venta: ";
        cin >> venta;

        if (i == 1) 
        {
            ventaMax = venta;
            ventaMin = venta;
            nombreMax = nombre;
            nombreMin = nombre;
        } else 
        {
            if (venta > ventaMax) 
            {
                ventaMax = venta;
                nombreMax = nombre;
            }
            if (venta < ventaMin) 
            {
                ventaMin = venta;
                nombreMin = nombre;
            }
        }
    }

    cout << "Vendedor con mayor venta: " << nombreMax << " con " << ventaMax << endl;
    cout << "Vendedor con menor venta: " << nombreMin << " con " << ventaMin << endl;

    return 0;
}