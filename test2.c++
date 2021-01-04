#include<stdlib.h>
#include<iostream>

using namespace std;
string nabidka[2];
string input1,input2,input3;

int pocet = 2;
bool tr = 0;

int main()
{
    nabidka[0] = "Polivka";
    nabidka[1] = "Svickova";
    nabidka[2] = "Spagety";
    cout << "Dobry den, jsem virtualni prodavac v C++, co to bude ?" << endl;   
    cout << "Nase nabidka: " << endl;
    for (int i = 0; i < pocet + 1; i++)
    {
        cout << nabidka[i] + " " << endl;
    }

    cin >> input1;
    cout << "Vybral jste si:" << endl;
    cout << input1 + " ";
    cout << "Hned to bude..." << endl;
   
    system("Pause");
  
    return 0;
}


