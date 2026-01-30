#include <iostream>
using namespace std;
int main(void)
{
    int expression = 1;
    switch (expression)
    {
    case 12:
        cout << "case 1";
        break; // Optional: prevents fall-through
    case 13:
        cout << "case 2";
        break;
    // ... any number of cases
    default:
        cout << "case 3";
        break; // Optional: no effect if default is last
    }
}