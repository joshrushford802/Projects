#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int bit_size = 512;
typedef uint8_t bite;

int main(int argc, char *argv[])
{

    if (argc < 2)
    {
        return 1;
        printf("Invalid: use only one command line argument\n");
    }

    FILE *file = fopen(argv[1], "r");

    if (file == NULL)
    {
        return 1;
        printf("unsuccessfull launch\n");
    }

    FILE *outpt = NULL;
    bite Buff[bit_size];
    char nm[8];
    int c = 0;

    while (fread(Buff, sizeof(bite), bit_size, file) == bit_size)
    {
        if (Buff[1] == 0xd8 && Buff[2] == 0xff && Buff[0] == 0xff)
        {
            if (c < 1)
            {
                sprintf(nm, "%03i.jpg", c);
                outpt = fopen (nm, "w");
                fwrite(Buff, sizeof(bite), bit_size, outpt);
                c++;
            }
            else if (c >= 1)
            {
                fclose(outpt);
                sprintf(nm, "%03i.jpg", c);
                outpt = fopen (nm, "w");
                fwrite(Buff, sizeof(bite), bit_size, outpt);
                c++;
            }
        }
        else if (c >= 1)
        {
            fwrite(Buff, sizeof(bite), bit_size, outpt);
        }
    }
    fclose(outpt);
    fclose(file);
}