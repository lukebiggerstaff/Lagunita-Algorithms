#include "stdio.h"

#define MAXN 45

long fib_ultimate(int n)
{
    int i;                  /* counter */
    long back2=0, back1=1;  /* last two values of f[n] */
    long next;              /* placeholder for sum */

    if (n == 0)
        return 0;

    for (i = 2; i < n; i++) {
       next = back1 + back2;
       back2 = back1;
       back1 = next;
    }
    
    return(back1+back2);
}

int main(int argc, char *argv[])
{
    long result = fib_ultimate(45);
    printf("%ld\n", result);
    return 0;
}
