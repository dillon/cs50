// Recovers JPEGs

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // check for correct usage
    if (argc != 2)
    {
        fprintf(stderr, "Usage: filename\n");
        return 1;
    }
    // declare variables
    unsigned char buffer[512] = {0};
    char filename[8] = {0};
    int filenumber = 0;
    FILE *outptr = NULL;

    // open card file
    FILE *inptr = fopen(argv[1], "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", argv[1]);
        return 2;
    }

    // read until end of card
    while (fread(buffer, sizeof(buffer), 1, inptr) == 1)
    {
        {
            // if start of new JPEG
            if (buffer[0] == 0xff &&
                buffer[1] == 0xd8 &&
                buffer[2] == 0xff &&
                (buffer[3] & 0xf0) == 0xe0)
            {
                if (outptr != NULL)
                {
                    fclose(outptr);
                    outptr = NULL;
                }
                // create new file
                sprintf(filename, "%03i.jpg", filenumber);

                // open the new file
                outptr = fopen(filename, "w");
                if (outptr == NULL)
                {
                    fprintf(stderr, "Failed to open %s.\n", filename);
                    return 1;
                }
                // write to the file
                fwrite(buffer, sizeof(buffer), 1, outptr);

                // increment filenumber
                filenumber++;
            }
            // if not start of new JPEG
            else
            {
                if (outptr != NULL)
                {
                    fwrite(buffer, sizeof(buffer), 1, outptr);
                }
                // else do nothing
            }
        }
    };
    if (outptr != NULL)
    {
        fclose(outptr);
    }
    if (inptr != NULL)
    {
        fclose(inptr);
    }
    return 0;
}