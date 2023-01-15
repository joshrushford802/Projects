#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int only_digits(int numbers);

int main(int argc, string argv[])
{
    if (argc < 2 || argc > 2)
    {
        printf("Usage: ./caesar key\n");
        return 0;
    }
    for (int n = 0; n < strlen(argv[1]); n++)
    {
        if (! isdigit(argv[1][n]))
        {
            printf("Usage: ./caesar key\n");
            return 0;
        }
    }
        int key = atoi(argv[1]);
        string message = get_string("Message: ");
        printf("ciphertext: \n");
    for(int up = 0; up < strlen(message); up++)
    {
        if (isupper(message[up]))
        {
            printf("%c", (message[up]-65+key)%26+65);
        }
        else if (islower(message[up]))
        {
            printf("%c", (message[up]-97+key)%26+97);
        }
        else
        {
            printf("%c", (message[up]));
        }
    }
        printf("\n");

}