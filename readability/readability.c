#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int main(void)
{

    string text = get_string("Text: ");

    float sentences = 0;
    float words = 0;
    //letters starts with 1 to account for the first letter of the string, which was not being included in the final count.
    float letters = 1;

    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == 46 || text[i] == 33 || text[i] == 63)
        {
            sentences++;
        }
        else if (text[i] == 32 || text[i] == text['\0'])
        {
            words++;
        }
        else if (text[i] != 34 && text[i] != 39 && text[i] != 40 && text[i] != 41 && text[i] != 44 && text[i] != 45 && text[i] != 58
                 && text[i] != 59 && text[i] != 92 && text[i] != 96)
        {
            letters++;
        }
    }

    float L = letters / words * 100;

    float S = sentences / words * 100;

    int grade = ceil(0.0588 * L - 0.296 * S - 15.8);

    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }
}