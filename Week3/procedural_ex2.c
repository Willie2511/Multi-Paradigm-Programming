#include <stdio.h>

int test(int x, int y)
{
    return x == 30 || y == 30 || (x + y == 30);
}

int main(void)
{
    printf("%d", test(28, 2));
    printf("\n%d", test(40, 4));
}