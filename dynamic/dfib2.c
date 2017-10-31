#include "stdio.h"

#define MAXN 45

long f[MAXN+1];

long fib_dp(int n)
{
    int i;          /* counter */
    long f[MAXN+1]; /* array to cache computed fib values */

    f[0] = 0;
    f[1] = 1;
    for (i = 2; i <= n; i++) {
        f[i] = f[i-1] + f[i-2];
    }

    return(f[n]);
}

int main(int argc, char *argv[])
{
    unsigned long result = fib_dp(45);
    printf("%lu\n", result);

    return 0;
}
