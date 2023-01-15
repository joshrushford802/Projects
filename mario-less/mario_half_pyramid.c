#include<cs50.h>
#include<math.h>
#include<stdio.h>

int main(void)
{
    int blocks;
    do
    {
        blocks = get_int("Height (between 1-8): ");
    }
    while (blocks > 8 || blocks < 1);


    for (int i = 0; i < blocks; i++)
    {
        if (blocks == 1)
        {
            printf("#\n");
            break;
        }
        else if (blocks == 2)
        {
            printf(" #\n");
            printf("##\n ");
            break;
        }
        else if (blocks == 3)
        {
            printf("   #\n");
            printf("  ##\n ");
            printf("###\n");
            break;
        }
        else if (blocks == 4)
        {
            printf("   #\n");
            printf("  ##\n ");
            printf("###\n");
            printf("####\n");
            break;
        }
        else if (blocks == 5)
        {
            printf("    #\n");
            printf("   ##\n ");
            printf(" ###\n");
            printf(" ####\n");
            printf("#####\n");
            break;
        }
        else if (blocks == 6)
        {
            printf("     #\n");
            printf("    ##\n ");
            printf("  ###\n");
            printf("  ####\n");
            printf(" #####\n");
            printf("######\n");
            break;
        }
        else if (blocks == 7)
        {
            printf("      #\n");
            printf("     ##\n ");
            printf("   ###\n");
            printf("   ####\n");
            printf("  #####\n");
            printf(" ######\n");
            printf("#######\n");
            break;
        }
        else if (blocks == 8)
        {
            printf("       #\n");
            printf("      ##\n ");
            printf("    ###\n");
            printf("    ####\n");
            printf("   #####\n");
            printf("  ######\n");
            printf(" #######\n");
            printf("########\n");
            break;
        }

    }
    printf("\n");
}