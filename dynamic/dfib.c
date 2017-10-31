#include <stdio.h>
#define MAXN 45 /* largest interest n */
#define UNKNOWN -1 /* contents denote an empty cell */

long f[MAXN+1];

long fib_c(int n)
{
    if (f[n] == UNKNOWN) 
       f[n] = fib_c(n-1) + fib_c(n-2); 
    
    return(f[n]);
}

long fib_c_driver(int n)
{
    int i;          /* counter */

    f[0] = 0;
    f[1] = 1;
    for (i = 2; i <= n; i++)  f[i] = UNKNOWN; 

    return(fib_c(n));
}

int main(int argc, char *argv[])
{
    unsigned long result = fib_c_driver(45);
    printf("%lu\n", result);

    return 0;
}
