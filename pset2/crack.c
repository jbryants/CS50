#define _XOPEN_SOURCE
#include <unistd.h>
#include <stdio.h>
#include <string.h>


static const char alpha[52] = "ETAOINSHRDLCUMWFGYPBVKJXQZetaoinshrdlcumwfgypbvkjxqz";


int main(int argc, char *argv[])
{
    char cracker[6] = { 0 };
    char salt[3] = { 0 };

    if (argc == 2)
    {
        salt[0] = argv[1][0];
        salt[1] = argv[1][1];
        char *hashPtr = argv[1];

        for (int i = 0; i < 52; i++)
        {
            cracker[0] = alpha[i];
            cracker[1] = '\0';

            if (strcmp(crypt(cracker, salt), hashPtr) == 0)
            {
                puts(cracker);
                return 0;
            }
            else
            {
                for (int j = 0; j < 52; j++)
                {
                    cracker[1] = alpha[j];
                    cracker[2] = '\0';
                    if (strcmp(crypt(cracker, salt), hashPtr) == 0)
                    {
                        puts(cracker);
                        return 0;
                    }
                    else
                    {
                        for (int k = 0; k < 52; k++)
                        {
                            cracker[2] = alpha[k];
                            cracker[3] = '\0';

                            if (strcmp(crypt(cracker, salt), hashPtr) == 0)
                            {
                                puts(cracker);
                                return 0;
                            }
                            else
                            {
                                for (int l = 0; l < 52; l++)
                                {
                                    cracker[3] = alpha[l];
                                    cracker[4] = '\0';

                                    if (strcmp(crypt(cracker, salt), hashPtr) == 0)
                                    {
                                        puts(cracker);
                                        return 0;
                                    }
                                    else
                                    {
                                        for (int m = 0; m < 52; m++)
                                        {
                                            cracker[4] = alpha[m];
                                            cracker[5] = '\0';

                                            if (strcmp(crypt(cracker, salt), hashPtr) == 0)
                                            {
                                                puts(cracker);
                                                return 0;
                                            }

                                        }

                                    }
                                }

                            }
                        }

                    }
                }

            }
        }
    }
    else
    {
        printf("Usage: %s hash\n", argv[0]);
        return 1;
    }

    return 0;
}
