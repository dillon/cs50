// cracks pwds

// salt is first 2 chars of argv[]
// hash is last 11 chars of argv[]

#define _XOPEN_SOURCE
#include <stdio.h>
#include <unistd.h>
#include <cs50.h>
#include <string.h>

// all chars rated by frequency of use in oxford dictionary, and including \0
char myDict[53] = "ZzQqJjXxKkVvBbYyWwGgPpFfMmUuCcDdLlHhRrSsNnIiOoAaTtEe\0";
char key[6] = "\0\0\0\0\0\0";
char salt[3] = "  \0";
string myArgument = "";
string myFunction();
string finalkey = "";

int main(int argc, string argv[])
{
    myArgument = argv[1];
    if (argc == 2 && strlen(argv[1]) == 13)
    {
        salt[0] = myArgument[0];
        salt[1] = myArgument[1];

        string finalKey = myFunction();
        // if it fails, return 1
        if (strcmp(finalkey, "00failed") == 0)
        {
            eprintf("Failed to find password\n");
            return (1);
        }
        // if it doesn't fail, print the finalKey and return 0;
        else
        {
            printf("%s\n", finalKey);
            return 0;
        }
    }
    // if arguments # is incorrect, fail and return 0
    else
    {
        printf("Usage: ./crack hash\n");
        return 1;
    }
    return 0;
}

string myFunction()
{
    // just 1
    for (int q = 51; q >= 0; q--)
    {
        key[0] = myDict[q];
        if (strcmp(crypt(key, salt), myArgument) == 0)
        {
            return key;
        }
        // done nesting
    }

    // just 2
    for (int q = 51; q >= 0; q--)
    {
        key[0] = myDict[q];
        if (strcmp(crypt(key, salt), myArgument) == 0)
        {
            return key;
        }
        // nest
        if (q != 52)
        {
            for (int qq = 52; qq >= 0; qq--)
            {
                key[1] = myDict[qq];
                if (strcmp(crypt(key, salt), myArgument) == 0)
                {
                    return key;
                }
                // done nesting
            }
        }
    }

    // just 3
    for (int q = 51; q >= 0; q--)
    {
        key[0] = myDict[q];
        if (strcmp(crypt(key, salt), myArgument) == 0)
        {
            return key;
        }
        // nest
        if (q != 52)
        {
            for (int qq = 52; qq >= 0; qq--)
            {
                key[1] = myDict[qq];
                if (strcmp(crypt(key, salt), myArgument) == 0)
                {
                    return key;
                }
                // nest
                if (qq != 52)
                {
                    for (int qqq = 52; qqq >= 0; qqq--)
                    {
                        key[2] = myDict[qqq];
                        if (strcmp(crypt(key, salt), myArgument) == 0)
                        {
                            return key;
                        }
                        // done nesting
                    }
                }
            }
        }
    }

    // just 4
    for (int q = 51; q >= 0; q--)
    {
        key[0] = myDict[q];
        if (strcmp(crypt(key, salt), myArgument) == 0)
        {
            return key;
        }
        // nest
        if (q != 52)
        {
            for (int qq = 52; qq >= 0; qq--)
            {
                key[1] = myDict[qq];
                if (strcmp(crypt(key, salt), myArgument) == 0)
                {
                    return key;
                }
                // nest
                if (qq != 52)
                {
                    for (int qqq = 52; qqq >= 0; qqq--)
                    {
                        key[2] = myDict[qqq];
                        if (strcmp(crypt(key, salt), myArgument) == 0)
                        {
                            return key;
                        }
                        // nest
                        if (qqq != 52)
                        {
                            for (int qqqq = 52; qqqq >= 0; qqqq--)
                            {
                                key[3] = myDict[qqqq];
                                if (strcmp(crypt(key, salt), myArgument) == 0)
                                {
                                    return key;
                                }
                                // done nesting
                            }
                        }
                    }
                }
            }
        }
    }

    // all 5
    for (int q = 51; q >= 0; q--)
    {
        key[0] = myDict[q];
        if (strcmp(crypt(key, salt), myArgument) == 0)
        {
            return key;
        }
        // nest
        if (q != 52)
        {
            for (int qq = 52; qq >= 0; qq--)
            {
                key[1] = myDict[qq];
                if (strcmp(crypt(key, salt), myArgument) == 0)
                {
                    return key;
                }
                // nest
                if (qq != 52)
                {
                    for (int qqq = 52; qqq >= 0; qqq--)
                    {
                        key[2] = myDict[qqq];
                        if (strcmp(crypt(key, salt), myArgument) == 0)
                        {
                            return key;
                        }
                        // nest
                        if (qqq != 52)
                        {
                            for (int qqqq = 52; qqqq >= 0; qqqq--)
                            {
                                key[3] = myDict[qqqq];
                                if (strcmp(crypt(key, salt), myArgument) == 0)
                                {
                                    return key;
                                }
                                // nest
                                if (qqqq != 52)
                                {
                                    for (int qqqqq = 52; qqqqq >= 0; qqqqq--)
                                    {
                                        key[4] = myDict[qqqqq];
                                        if (strcmp(crypt(key, salt), myArgument) == 0)
                                        {
                                            return key;
                                        }
                                        // done nesting
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    return "00failed";
}
