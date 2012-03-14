#include <stdio.h>

#define M 40000000
#define L 25

unsigned long long phis[M];

int main(void)
{
    unsigned long long p, m;
    unsigned long long s = 0;
    for (p = 0; p < M; p++) phis[p] = p;
    for (p = 2; p < M; p++) {
        if (phis[p] == p) {
            for (m = p+p; m < M; m += p)
                phis[m] -= phis[m]/p;
            if ((phis[p] = phis[p-1]+1) == L)
                s += p;
        } else {
            phis[p] = phis[phis[p]]+1;
        }
    }
    printf("%llu\n", s);
}

