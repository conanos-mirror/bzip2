#include <bzlib.h>
#include <stdio.h>
int main(void)
{
    printf("BZip2 : %s",BZ2_bzlibVersion());
    return 0;
}