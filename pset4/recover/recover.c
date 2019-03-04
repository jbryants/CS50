#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>


int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover image\n");
        return 1;
    }

    // open input file
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", argv[1]);
        return 2;
    }

    uint8_t buffer[512];
    char filename[8];
    int fcount = 0;

    // file pointer for JPEGs
    FILE *img = NULL;

    // iterates over file
    while (fread(buffer, 512, 1, file))
    {
        // checks if first four bytes are jpeg
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (img != NULL)
            {
                fclose(img);
            }

            // makes new jpeg
            sprintf(filename, "%03i.jpg", fcount);

            // opens new file to write in
            img = fopen(filename, "w");

            fcount++;
        }

        // writes bytes to new JPEG file
        if (img != NULL)
        {
            fwrite(buffer, 512, 1, img);
        }
    }

    // closes files
    fclose(img);
    fclose(file);

    // success
    return 0;
}