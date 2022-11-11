#include <stdio.h>
#include <stdlib.h>

int test(int x, int y)
{
    return x == 5 || y == 5 || x + y == 5 || abs(x - y) == 5;
}

int main(void)
{
    printf("%d", test(5, 4));
    printf("\n%d", test(4, 3));
    printf("\n%d", test(1, 4));
}
