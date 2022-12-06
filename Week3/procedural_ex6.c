#include <stdio.h>
#include <stdlib.h>

void testRightmostDigit(int x, int y)
{
    int digit1 = abs(x) % 10;
    int digit2 = abs(y) % 10;
    if (digit1 == digit2)
    {
        printf("\nRightmost Digits are equal");
    }
    else
    {
        printf("\nRightmost Digits are not equal");
    }
}

int main(void)
{

    testRightmostDigit(12, 22);
}