// Encrypts with Vigenere
// consider using atoi, isalpha, isupper, islower, (x-65) % 26, (x-97) % 26
// doesn't use atoi!
#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>


int main(int argc, string argv[])
{
    if (argc == 2)
    {
        // check that key is ok
        for (int j = 0; j < strlen(argv[1]); j++)
        {
            if (!isalpha(argv[1][j]))
            {
                eprintf("error: key is invalid.\n");
                exit(1);
            }
        }
        string k = get_string("Enter your message: ");

        // declare variables for encryption process
        int y = 0;
        int val = 0;
        int kval = 0;
        // encrypt and print
        printf("ciphertext: ");
        for (int i = 0; i < strlen(k); i++)
        {
            if (isalpha(k[i]))
            {
                if (isupper(k[i]))
                {
                    kval = toupper(argv[1][y]) - 65;
                    val = (k[i] - 65 + kval) % 26;
                    y = (y + 1) % (strlen(argv[1]));
                    printf("%c", val + 65);
                }
                else if (islower(k[i]))
                {
                    {
                        kval = toupper(argv[1][y]) - 65;
                        val = (k[i] - 97 + kval) % 26;
                        y = (y + 1) % (strlen(argv[1]));
                        printf("%c", val + 97);
                    }
                }
                else
                {
                    printf("%c", k[i]);
                }
            }
            else
            {
                printf("%c", k[i]);
            }
        }
    }
    else
    {
        eprintf("error: too few or too many arguments\n");
        exit(1);
    }
    // print new line
    printf("\n");
    exit(0);
}
