/*
 * Calculator.cpp
 *
 *  Date: [1/10/2023]
 *  Author: [Joshua D Rushford]
 */

#include <iostream>
#include <string>

using namespace std;

int main() // This must be specified as type "int", not as "void".
{
	char statement[100];
	float op1;
    float op2;
	char operation;
	char answer='Y'; /*
                      Since this is a char it uses single quotes (''), not double ("").
                      It was also missing a semicolon (;).
                    */

	while (tolower(answer) =='y') // Added some code so it responds to y regardless of capitalization.
								  // To do this, I also had to include the <string> library above.
	{
		cout << "Enter expression" << endl; // Missing a space between << and endl. This won't break the program, however it's messy code.
		cin >> op2;
        cin >> operation;
        cin >> op1;

        // All of the "if" statements were missing curly brackets ({}).
		if (operation == '+') { // Char needs be have single quotes (''), not double ("").
			cout << op1 << " + " << op2 << " = " << op1 + op2 << endl; // Had a >> when it needs to be <<.
        }
		if (operation == '-') {
			cout << op1 << " - " << op2 << " = " << op1 - op2 << endl; // Had a >> when it needs to be <<.
        }
		if (operation == '*') {
			cout << op1 << " / " << op2 << " = " << op1 * op2 << endl; // Missing a semicolon (;) at the end of this line.
        }
		if (operation == '/') {
			cout << op1 << " * " << op2 << " = " << op1 / op2 << endl;
        }

		cout << "Do you wish to evaluate another expression? " << endl;
		cin >> answer;
	}

	cout << "Program Finished." << endl; // Added a new line to denote to the user the end of the program.
	
	return 0;
}
