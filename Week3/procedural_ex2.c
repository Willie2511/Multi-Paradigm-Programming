#include <stdio.h>

int testThirty(int x, int y)
{
    return x == 30 || y == 30 || (x + y == 30);
}

int main(void)
{
    printf("%d", testThirty(28, 2));
    printf("\n%d", testThirty(40, 4));
}