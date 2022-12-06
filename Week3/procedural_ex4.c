#include <stdio.h>
#include <stdlib.h>

int testOfFives(int a, int b)
{
    return a == 5 || b == 5 || (a + b == 5) || abs(a - b) == 5;
}

int main(void)
{
    printf("%d", testOfFives(10, 15));
    printf("\n%d", testOfFives(2, 3));
}