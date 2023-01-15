#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    float change;
    do
    {
        change = get_float("Change due to customer: ");
    }
    while (change < 0);

    int cents = round(change * 100);
    int coins = 0;

    //number of quarters
    while (cents >= 25)
    {
        cents -= 25;
        coins++;
    }
    //number of dimes
    while (cents >= 10)
    {
        cents -= 10;
        coins++;
    }
    //number of nickles
    while (cents >= 5)
    {
        cents -= 5;
        coins++;
    }
    //number of pennies
    while (cents >= 1)
    {
        cents -= 1;
        coins++;
    }

    printf("Number of coins owed to customer: %i\n", coins);
}