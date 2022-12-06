#include <stdio.h>
#include <stdlib.h>

void testTwoConditions(int x, int y, int z)
{
    if (y > x && z > y)
    {
        printf("\nYes conditions are met");
    }
    else
    {
        printf("\nNo conditions are not met\n");
    }
}

int main(void)
{
    testTwoConditions(10, 15, 2);
    testTwoConditions(2, 3, 8);
}