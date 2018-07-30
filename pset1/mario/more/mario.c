#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int n;
    do
    {
        // prompt
        n = get_int("Enter a positive integer less of 23 or less: ");
    }
    // repeat if incorrect input
    while (n < 0 || n > 23);
    // forloop for each row
    for (int i = 0; i < n; i++)
    {
        // calculate leading space and hash numbers
        int space = n - (i + 1);
        int hash = n - space;

        // print leading spaces
        for (int j = 0; j < space; j++)
        {
            printf(" ");
        }
        // print first set of hashes
        for (int k = 0; k < hash; k++)
        {
            printf("#");
        }
        // print standard 2-space separator
        printf("  ");
        // print second set of hashes
        for (int k = 0; k < hash; k++)
        {
            printf("#");
        }
        // new line to prep for next row forloop
        printf("\n");
    }
}
