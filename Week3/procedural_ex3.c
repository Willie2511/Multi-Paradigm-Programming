#include <stdio.h>
#include <stdlib.h>

int testWithinRange(int a, int b)
{
    return a + b >= 10 && a + b <= 20 ? 30 : a + b;
}

int main(void)
{
    printf("%d", testWithinRange(12, 17));
    printf("\n%d", testWithinRange(2, 17));
}
