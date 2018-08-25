#include<stdio.h>
#include<string.h>
#include<cs50.h>
#include<ctype.h>

char ucAlp[27] = { 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' };
char lcAlp[27] = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' };
int key[100];
int count;

void setNcount(char **argv);
void cipher(char *pt);

int main(int argc, char *argv[])
{
    char pt[100];

    if (argc == 2)
    {
        setNcount(argv);

        printf("plaintext:  ");
        scanf("%[^\n]%*c", pt);

        cipher(pt);
    }
    else
    {
        printf("Usage: %s k\n", argv[0]);
        return 1;
    }

    return 0;
}


void setNcount(char **argv)
{
    int length = strlen(argv[1]);
    char upper;

    for (int i = 0; i < length; i++)
    {
        if (isalpha(argv[1][i]))
        {
            upper = toupper(argv[1][i]);

            for (int j = 0; j < 26; j++)
            {
                if (upper == ucAlp[j])
                {
                    key[i] = j;
                    count++;
                    break;
                }
            }

        }
        else
        {
            printf("Usage: %s k\n", argv[0]);
            exit(1);
        }
    }

    return;
}



void cipher(char *pt)
{
    int keyIndex = 0;
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
                        index = (j + key[keyIndex % count]) % 26;
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
                        index = (j + key[keyIndex % count]) % 26;
                        printf("%c", lcAlp[index]);
                        break;
                    }
                }
            }

            keyIndex++;
        }
        else
        {
            printf("%c", pt[i]);
        }
    }

    printf("\n");
}
