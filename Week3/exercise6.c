#include <stdio.h>
#include <stdlib.h>

int test(int x, int y, int z)
{
    return x % 10 == y % 10 || x % 10 == z % 10 || y % 10 == z % 10;
}
int main(void)
{
    printf("%d", test(11, 21, 31));
    printf("\n%d", test(11, 22, 31));
    printf("\n%d", test(11, 22, 33));
}
