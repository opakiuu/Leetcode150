#include <iostream>
using namespace std;

int main()
{
    int number = 0;

    // The loop body runs at least once to get user input
    do
    {
        cout << "Enter a number: " << endl;
        cin >> number;
    } while (number == 0);

    cout << "You entered: " << number << ". Exiting loop." << std::endl;

    return 0;
}
