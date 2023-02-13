// Joshua D Rushford
// 2/12/2023

#include <iostream>
#include <iomanip>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
#include <chrono>
#include <thread>
using namespace std;
using namespace std::this_thread;
using namespace std::chrono_literals;


void optionOne() {
    string inputWord, file;
    ifstream inFS;
    int counter = 0;

    // Ensure file is opened without error.
    inFS.open("input.txt");
    if (!inFS.is_open()) {
        cout << "An error occured while opening file." << endl;
    }

    // Request user to enter a word.
    cout << endl << "Enter a word: " << endl;
    cout << "> ";
    cin >> inputWord;

    // Iterate through the list, adding 1 to the counter variable every time the entered word is found.
    while (inFS >> file) {
        if (inputWord == file) {
            counter++;
        }
    }

    // Display how many times the word is found.
    cout << "Frequency: " << counter << endl << endl;

    inFS.close();
}


void optionTwo() {
    vector <string> file;
    vector <string> compareFile;
    string word;
    ifstream inFS;
    int counter;

    cout << endl;

    // Ensure the file is opened without error.
    inFS.open("input.txt");
    if (!inFS.is_open()) {
        cout << "An error occured while opening file." << endl;
    }

    // Store contents of the file in a variable, then transfer those contents to a vector.
    for (int k = 0; k < 104; ++k) {
        inFS >> word;
        file.push_back(word);
    }

    // Count the number of occurances an item is repeated in the file.
    for (int j = 0; j < file.size(); j++) {
        counter = 0;

        for (int i = 0; i < file.size(); ++i) {
            if (file.at(j) == file.at(i)) {
                counter++;
            }
        }

        // Compare the two vectors and, if the item is not in the comparison vector, add it and display it's
        // count, otherwise fill it with an empty string so an error doesn't occur.
        if (find(compareFile.begin(), compareFile.end(), file.at(j)) == compareFile.end()) {
            compareFile.push_back(file.at(j));
            cout << setfill(' ') << setw(11) << compareFile.at(j) << ' ' << counter << endl;
        }
        else {
            compareFile.push_back("");
        }
    }

    cout << endl;

    inFS.close();
}

void optionThree() {
    vector <string> file;
    vector <string> compareFile;
    string word;
    ifstream inFS;
    int counter;

    cout << endl;

    // Ensure the file is opened without error.
    inFS.open("input.txt");
    if (!inFS.is_open()) {
        cout << "An error occured while opening file." << endl;
    }

    // Store contents of the file in a variable, then transfer those contents to a vector.
    for (int k = 0; k < 104; ++k) {
        inFS >> word;
        file.push_back(word);
    }

    // Count the number of occurances an item is repeated in the file.
    for (int j = 0; j < file.size(); j++) {
        counter = 0;

        for (int i = 0; i < file.size(); ++i) {
            if (file.at(j) == file.at(i)) {
                counter++;
            }
        }

        // Compare the two vectors and, if the item is not in the comparison vector, add it and display it's
        // count in the form of a histogram, otherwise fill it with an empty string so an error doesn't occur.
        if (find(compareFile.begin(), compareFile.end(), file.at(j)) == compareFile.end()) {
            compareFile.push_back(file.at(j));
            cout << setfill(' ') << setw(11) << compareFile.at(j) << ' ';

            for (int g = 0; g < counter; ++g) {
                cout << '*';
            }

            cout << endl;
        }
        else {
            compareFile.push_back("");
        }
    }

    cout << endl;

    inFS.close();
}


void menu() {
    int inputNum;

    cout << "***************Corner Grocer***************" << endl;
    cout << "-------------------------------------------" << endl;
    cout << "    Choose from the following menu . . ." << endl << endl;

    while (true) {
        // Display available options after every action is complete.
        cout << "    Word Frequency:                                    Enter 1" << endl;
        cout << "    Frequency of All Items Purchased:                  Enter 2" << endl;
        cout << "    Histogram of the Frequency of All Items Purchased: Enter 3" << endl;
        cout << "    Quit Program:                                      Enter 4" << endl;
        cout << "    > ";
        cin >> inputNum;

        // Execute an action based on the user input. Also, validate user
        // input so no errors occur.
        if (inputNum != 1 && inputNum != 2 && inputNum != 3 && inputNum != 4) {
            cout << "Invalid response . . ." << endl;
            cin.clear();
            cin.ignore();
        }
        else {
            if (inputNum == 1) {
                optionOne();
                cin.clear();
                cin.ignore();
            }
            else if (inputNum == 2) {
                optionTwo();
                cin.clear();
                cin.ignore();
            }
            else if (inputNum == 3) {
                optionThree();
                cin.clear();
                cin.ignore();
            }
            else if (inputNum == 4) {
                // This code sequence uses a scheduled delay in code execution for a more
                // "cinematic" exit of the program.
                cout << endl << "Exiting The Program" << endl;
                sleep_for(2s);
                cout << " . . . . ." << endl;
                sleep_for(2s);
                cout << "Goodbye!" << endl << endl;
                break;
            }
        }
    }
}


int main() {

    menu();

    return 0;
}
