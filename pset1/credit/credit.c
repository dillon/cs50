#include <stdio.h>
#include <cs50.h>

int luhn(long long i);
int nlength = 0;
int main(void)
{
    long long n = get_long_long("Enter your parent's credit card number: ");
    // a switch to check first two digits

    if (luhn(n) % 10 == 0)
    {
        switch (nlength)
        {
            case 15 :
                // if 15 numbers, are first two 34 or 37
                if ((n / 10000000000000) == 34 || (n / 10000000000000) == 37)
                {
                    printf("AMEX\n");
                }
                else
                {
                    printf("INVALID\n");
                }
                break;
            case 16:
                // if 16 numbers, is first 4
                if ((n / 1000000000000000) == 4)
                {
                    printf("VISA\n");
                }
                // else if 16 numbers, are first two 51, 52, 53, 54, or 55
                else if ((n / 100000000000000) > 50 && (n / 100000000000000) < 56)
                {
                    printf("MASTERCARD\n");
                }
                else
                {
                    printf("INVALID\n");
                }
                break;
            case 13:
                // if 13 numbers, is first 4?
                if ((n / 1000000000000) == 4)
                {
                    printf("VISA\n");
                }
                else
                {
                    printf("INVALID\n");
                }
                break;
            default:
                printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}

int luhn(long long i)
{
    int finalval = 0;
    long long firsti = i / 10; // get rid of last number
    long long secondi = i; // take i as is
    if (firsti >= 10)
    {
        while (firsti > 0)
        {
            // add every other number*2
            int tempval = (firsti % 10) * 2;
            finalval += (tempval / 10 + tempval % 10);
            nlength += 1;
            firsti = firsti / 100;
        }
        while (secondi > 0)
        {
            // add every other number
            finalval += secondi % 10;
            nlength += 1;
            secondi = secondi / 100;
        }
        return finalval;
    }
    else
    {
        printf("INVALID\n");
        return 0;

    }
}