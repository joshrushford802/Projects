// Joshua D Rushford
// 2/5/2023

#include <iostream>
#include <iomanip>
#include <string>
#include <fstream>
#include <math.h>
using namespace std;


void displayInfo() {
    cout << "*********************************************" << endl;
    cout << "******************Data Input*****************" << endl;
}


void staticReportWithout() {
    cout << "Balance and Interest Without Additional Monthly Deposits" << endl;
    cout << "========================================================" << endl;
    cout << "Year       Year End Balance     Year End Earned Interest" << endl;
    cout << "--------------------------------------------------------" << endl;
}


void staticReportWith() {
    cout << "Balance and Interest With Additional Monthly Deposits" << endl;
    cout << "========================================================" << endl;
    cout << "Year       Year End Balance     Year End Earned Interest" << endl;
    cout << "--------------------------------------------------------" << endl;
}


int main() {
    string throwAway;
    float initAmt, numYears, annInt, monDep, percentage, yearEndBal, yearEndEarnedInt, increase, yearEndBalLast;
    int i;

    // Initialize all user inputs to -1 in order to force them into a user validation loop.
    initAmt = -1;
    monDep = -1;
    annInt = -1;
    numYears = -1;
    percentage = annInt / 100;
    yearEndBal = initAmt;
    yearEndEarnedInt = percentage;
    yearEndBalLast = initAmt;

    // Display the program header. This is urely for cosmetics.
    displayInfo();

    // Each user input is tested to validate that the entered input is a number.
    cout << "Initial Investment Amount: $";
    while (!(cin >> initAmt) || initAmt == -1) {
        cout << "Initial Investment Amount: $";
        cin >> initAmt;
        cin.clear();
        cin.ignore();
    }

    cout << "Monthly Deposit: $";
    while (!(cin >> monDep) || initAmt == -1) {
        cout << "Monthly Deposit: $";
        cin >> monDep;
        cin.clear();
        cin.ignore();
    }

    cout << "Annual Interest: %";
    while (!(cin >> annInt) || initAmt == -1) {
        cout << "Annual Interest: %";
        cin >> annInt;
        cin.clear();
        cin.ignore();
    }

    cout << "Number of Years: ";
    while (!(cin >> numYears) || initAmt == -1) {
        cout << "Number of Years: ";
        cin >> numYears;
        cin.clear();
        cin.ignore();
    }

    cout << "Enter anything to continue . . ." << endl;
    // Store any input in a variable in order for the user to continue through the next part of the program.
    cin >> throwAway;

    // Calculate and print the chart for the first report.
    staticReportWithout();
    percentage = annInt / 100;
    yearEndBal = initAmt;
    yearEndEarnedInt = percentage;
    yearEndBalLast = initAmt;

    for (i = 1; i <= numYears; ++i) {
        percentage = annInt / 100;
        increase = initAmt * percentage;
        yearEndBal += increase;
        yearEndEarnedInt = yearEndBal - yearEndBalLast;

        cout << fixed << setprecision(2);

        cout << "  " << i << "                  $" << yearEndBal << "                   $" << yearEndEarnedInt << endl << endl;

        yearEndBalLast = yearEndBal;

    }

    cout << "========================================================" << endl << endl << endl;

    // Calculate and print the chart for the second report.
    staticReportWith();

    yearEndBal = initAmt + (monDep * 12);
    yearEndEarnedInt = percentage;
    increase = initAmt + monDep * percentage;
    yearEndBalLast = (monDep * 12) - initAmt + increase;

    for (i = 1; i <= numYears; ++i) {
        percentage = annInt / 100;
        increase = initAmt + monDep * percentage;
        yearEndBal += increase;
        yearEndEarnedInt = yearEndBal - yearEndBalLast;

        cout << fixed << setprecision(2);

        cout << "  " << i << "                  $" << yearEndBal << "                   $" << yearEndEarnedInt << endl << endl;

        yearEndBalLast = yearEndBal;

    }

    cout << "========================================================" << endl << endl;

    return 0;
}