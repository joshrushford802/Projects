#include <iostream>
#include <iomanip>
#include <string>
#include <fstream>
using namespace std;


int main() {
    ifstream inFS("FahrenheitTemperature.txt"); // Open the file and store it in a variable.
    ofstream outFS("CelsiusTemperature.txt");   // Assign the outfile to a variable.
    string city;
    double F;
    double celsius;

    // Ensure the file was opened successfully.
    if(!inFS.is_open()) {
        cout << "Failure to open file" << endl;
        return 1;
    }

    // Loop through the file, modify the numbers, and output the results to the outfile.
    while (inFS >> city >> F) {
        celsius = (F - 32) * 5 / 9;
        outFS << city << ' ' << celsius << endl;
    }

    // Close the file we just read from.
    inFS.close();

    return 0;
}