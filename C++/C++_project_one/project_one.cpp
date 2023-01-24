// Joshua D Rushford
// 1/22/2023

#include <iostream>
#include <iomanip>
#include <string>
using namespace std;


// This function adds the top and bottom walls for the instructions and both clocks.
string nCharString() {
    string n = "***************************";

    return n;
}


// This function displays the instructions to the user.
void DisplayInstructions() {

    cout << nCharString() << endl;
    cout << "* 1 - Add One Hour        *" << endl;
    cout << "* 2 - Add One Minue       *" << endl;
    cout << "* 3 - Add One Second      *" << endl;
    cout << "* 4 - Exit Program        *" << endl;
    cout << nCharString() << endl;

}


// Print the 12-hour clock.
void Print12HrClock(int hr, int min, int sec, string am_or_pm) {
    cout << nCharString() << endl;
    cout << "*      12-Hour Clock      *" << endl;
    cout << "*       " << setfill('0') << setw(2) << hr << ":" << setfill('0') << setw(2) << min << ":" << setfill('0') << setw(2) << sec << " " << am_or_pm << "       *" << endl;
    cout << nCharString() << endl;
}


// Print the 24-hour clock.
void Print24HrClock(int hr1, int min, int sec) {
    cout << nCharString() << endl;
    cout << "*      24-Hour Clock      *" << endl;
    cout << "*        " << setfill('0') << setw(2) << hr1 << ":" << setfill('0') << setw(2) << min << ":" << setfill('0') << setw(2) << sec << "         *" << endl;
    cout << nCharString() << endl;
}


// This function utilizes a loop to ask for user input until the user enters an input that breaks the loop and ends the
// program. The if-statement nested in the loop performs input validation as well as processes each correct user input
// to add hours, minutes, and seconds to both clocks in this program.
void UserInput() {
    unsigned int choice;
    unsigned int user_input;
    unsigned int hr = 0;
    unsigned int hr1 = 0;
    unsigned int min = 0;
    unsigned int sec = 0;
    string am_or_pm = "AM";

    while (true) {

        // This is just a divider to make it easier/ clearer to the user what each of their past inputs were.
        // This is merely for a better user experience.
        cout << endl;
        cout << "--------------------------------------------------------------------------------------------------" << endl;
        cout << endl;

        DisplayInstructions();
        cout << endl;
        cout << "Input: ";
        cin >> user_input;

        // Validate input. If it is below 1 or above 4, or if it is not a number, return an error message,
        // clear cin to avoid an infinite loop, and reprompt.
        if (user_input < 1 || user_input > 4) {
            cout << "Invalid input, please try again." << endl;
            cin.clear();
            cin.ignore(10000,'\n');
        }
        else if (user_input == 1) {
            hr++;
            hr1++;
        }
        else if (user_input == 2) {
            min++;
        }
        else if (user_input == 3) {
            sec++;
        }
        else if (user_input == 4) {
            break;
        }

        // This series of if-statements enables incrementing based on the number of the seconds, minutes and hours.
        // For example, an if-statment in this block will increment minutes up by one and reset seconds to 0 when
        // seconds get past 59. The same is true for hours, abiding ny the respective rules of the clock.
        // This block also determines and sets whether it's morning (AM) or afternoon (PM).
        if (sec > 59) {
            min++;
            sec = 0;
        }

        if (min > 59) {
            hr++;
            hr1++;
            min = 0;
        }

        if (hr == 12 && am_or_pm == "AM" && hr1 == 12) {
            am_or_pm = "PM";
        }

        if (hr > 12) {
            hr = 1;
        }

        if (hr1 > 23) {
            hr1 = 0;
        }

        if (hr == 12 && am_or_pm == "PM" && hr1 == 0) {
            am_or_pm = "AM";
        }

        if (hr > 12) {
            hr = 1;
        }

        // Call the functions to print both clocks to see changes after each input.
        Print12HrClock(hr, min, sec, am_or_pm);
        Print24HrClock(hr1, min, sec);
    }
}


int main() {
    int user_input;

    // Call the function that ties all the other functions together and produces output.
    UserInput();


    return 0;
}