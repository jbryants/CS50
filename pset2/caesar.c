#include<stdio.h>
#include<cs50.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>

void cipher(char *pt, int key);

int main(int argc, char *argv[])
{
    char pt[100];
    int key = 0;

    if (argc == 2)
    {
        key = atoi(argv[1]);

        printf("plaintext:  ");
        scanf("%[^\n]%*c", pt);

        cipher(pt, key);
    }
    else
    {
        printf("Usage: %s k\n", argv[0]);
        return 1;
    }

    return 0;
}


void cipher(char *pt, int key)
{
    char ucAlp[27] = { 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' };
    char lcAlp[27] = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' };
    int index;

    int length = strlen(pt);

    printf("ciphertext: ");
    for (int i = 0; i < length; i++)
    {
        if (isalpha(pt[i]))
        {
            if (isupper(pt[i]))
            {
                for (int j = 0; j < 26; j++)
                {
                    if (pt[i] == ucAlp[j])
                    {
                        index = (j + key) % 26;
                        printf("%c", ucAlp[index]);
                        break;
                    }
                }
            }
            else if (islower(pt[i]))
            {
                for (int j = 0; j < 26; j++)
                {
                    if (pt[i] == lcAlp[j])
                    {
                        index = (j + key) % 26;
                        printf("%c", lcAlp[index]);
                        break;
                    }
                }
            }
        }
        else
        {
            printf("%c", pt[i]);
        }
    }

    printf("\n");

    return;
}
