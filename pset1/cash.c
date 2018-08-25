#include<stdio.h>
#include<cs50.h>
#include<math.h>

int get_coins(int);

int main(void)
{
    float dollars;
    int cents;

    do
    {
        dollars = get_float("Change owed: ");
    }
    while (dollars < 0);

    cents = (float)round(dollars * 100);

    printf("%i\n", get_coins(cents));

    return 0;
}

int get_coins(int cents)
{

    int coins = 0;
    int denom[] = {25, 10, 5, 1};

    for (int i = 0; i < 4; i++)
    {
        coins += cents / denom[i];
        cents %= denom[i];
    }

    return coins;
}
