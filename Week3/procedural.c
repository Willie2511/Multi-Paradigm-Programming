#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int difference(int n)
{
    int x = 51;
    n = abs(n);

    if (n > x)
    {
        return (n - x) * 3;
    }
    return x - n;
}

int main(void)
{
    printf("Difference is %d", difference(53));
    printf("\nDifference is %d", difference(-30));
}
