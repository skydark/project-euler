// gcc -o 211 -lm 211.c -std=c99 && time ./211
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define N 64000000

typedef unsigned long long int ulli;

int main(void)
{
    ulli k = 0, s = 0, n = N;
    ulli *pool = (ulli*)malloc(sizeof(ulli) * n);
    for (k = 1; k < n; k++)
        pool[k] = 1;
    for (k = 2; k < n; k++) {
        ulli k2 = k * k;
        for (int m = k; m < n; m += k) {
            pool[m] += k2;
        }
    }
    for (k = 1; k < n; k++) {
        ulli x = pool[k];
        ulli t = floor(sqrt(x));
        if (t * t == x)
            s += k;
    }
    printf("%llu", s);
    free(pool);
    return 0;
}
