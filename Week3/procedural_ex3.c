#include <stdio.h>
#include <stdlib.h>

int test(int a, int b)
{
    return a + b >= 10 && a + b <= 20 ? 30 : a + b;
}

int main(void)
{
    printf("%d", test(12, 17));
    printf("\n%d", test(2, 17));
}
