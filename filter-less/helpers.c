#include "helpers.h"
#include <math.h>
#define Green 1
#define Blue 2
#define Red 0

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int g = round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3);
            image[i][j].rgbtRed = g;
            image[i][j].rgbtBlue = g;
            image[i][j].rgbtGreen = g;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int red = round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue);
            int blue = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue);
            int green = round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue);

            image[i][j].rgbtGreen = fmin(255, green);
            image[i][j].rgbtBlue = fmin(255, blue);
            image[i][j].rgbtRed = fmin(255, red);
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE c;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width * .5; j++)
        {
            c = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = c;
        }
    }
    return;
}

// Blur image
int recieve(int x, int y, int width, int height, int colors, RGBTRIPLE image[height][width])
{
    int equals = 0;
    float tally = 0;

    for (int i = x - 1; i <= x + 1; i++)
    {
        for (int k = y - 1; k <= y + 1; k++)
        {
            if (k >= width || k < 0 || i >= height || i < 0)
            {
                continue;
            }
            if (colors == Green)
            {
                equals += image[i][k].rgbtGreen;
            }
            else if (colors == Red)
            {
                equals += image[i][k].rgbtRed;
            }
            else
            {
                equals += image[i][k].rgbtBlue;
            }
            tally++;
        }
    }
    return floor(equals / tally);
}

void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE q[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            q[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtGreen = recieve(i, j, width, height, Green, q);
            image[i][j].rgbtBlue = recieve(i, j, width, height, Blue, q);
            image[i][j].rgbtRed = recieve(i, j, width, height, Red, q);
        }
    }
    return;
}