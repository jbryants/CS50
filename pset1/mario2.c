#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int flag;

    do
    {
        int n = get_int("Height: ");

        if ((n > 0) && (n <= 23))
        {
            for (int i = 0; i < n; i++)
            {

                for (int j = i; j < (n - 1); j++)
                {
                    printf(" ");
                }

                for (int k = 0; k < (i + 1); k++)
                {
                    printf("#");
                }

                printf("  ");

                for (int k = 0; k < (i + 1); k++)
                {
                    printf("#");
                }

                printf("\n");
            }
            flag = 1;
        }
        else
        {
            flag = 0;
        }

    }
    while (flag < 1);

    return 0;
}
