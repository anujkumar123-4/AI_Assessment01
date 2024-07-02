#include <iostream>
using namespace std;
int main()
{
    char op;
    double n1, n2;
    cout << "Enter Operators(+, -, *, /): ";
    cin >> op;
    cout << "Enter the two numbers: ";
    cin >> n1 >> n2;
    switch (op)
    {
    case '+':
        cout << "Result: " << n1 + n2;
        break;
    case '-':
        cout << "Result: " << n1 - n2;
        break;
    case '*':
        cout << "Result: " << n1 * n2;
        break;
    case '/':
        if (n2 != 0)
            cout << "Result: " << n1 / n2;
        else
            cout << "Error! Division by zero";
        break;

    default:
        cout << "Error! Invalid Number";
    }
}