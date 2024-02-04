#include "Root.h" //including our header file

using namespace std;


/**
 * menu - simple terminal menu interface
*/

void menu(){
    int choice;
    string expression;

    cout << "--------- Welcome to the Root finder --------------\n";
    cout << "Please insert the function to find roots (refer manual for function syntax):\n";
    cin >> expression;
    cout << "which method are you using?\n";
    cout << "1. Bisection Method\n";
    cout << "2. Newton-Raphson Method\n";

    switch (choice)
    {
    case 1:
        // code here //
        break;
    case 2:
        // code here //
        break;
    default:
        break;
    }
}

/**
 * main - program starts here
 * Returns: 1 after completion
*/
int main(){
    menu();
}
