#include<stdio.h>
#include<cs50.h>

int main(void)
{
    string p = get_string("Type a paragraph:\n");

    int chars = 0;
    while(p[chars] != '\0')
    {
        chars++;
    };

    printf("Number of characters: %i\n", chars);
}