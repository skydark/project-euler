/*
 * The radical of n, rad(n), is the product of distinct prime factors of n. For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.

 * We shall define the triplet of positive integers (a, b, c) to be an abc-hit if:

    #GCD(a, b) = GCD(a, c) = GCD(b, c) = 1
    #a < b
    #a + b = c
    #rad(abc) < c

 * For example, (5, 27, 32) is an abc-hit, because:

    #GCD(5, 27) = GCD(5, 32) = GCD(27, 32) = 1
    #5 < 27
    #5 + 27 = 32
    #rad(4320) = 30 < 32

 * It turns out that abc-hits are quite rare and there are only thirty-one abc-hits for c < 1000, with ∑c = 12523.

 * Find ∑c for c < 120000.

 * Note: This problem has been changed recently, please check that you are using the right parameters.

 * Answer:
	#18407904
*/

#include <stdio.h>
#include <math.h>

#define M 120000

int rad[M];

int gcd(int m, int n)
{
	int swap;
	if (m == n) return m;
	if (m > n) {
		swap = m; m = n; n = swap;
	}
	if (m == 0) return n;
	if (m == 1) return 1;
	return gcd(n % m, m);
}

int main()
{
	long long int s = 0, pp;
	int a, b, c, p, q, qq, cc, isqrtp;

	rad[1] = 1;
	for (p = 2; p < M; p++) {
		if (rad[p] > 0) continue;
		isqrtp = sqrt(p);
		for (q = 2; q <= isqrtp; q++) {
			if (p % q == 0) {
				pp = p;
				while (pp % q == 0)
					pp /= q;
				qq = q * rad[pp];
				pp = p;
				while (pp < M) {
					rad[pp] = qq;
					pp *= q;
				}
				break;
			}
		}
		if (q > isqrtp) {
			pp = p;
			while (pp < M) {
				rad[pp] = p;
				pp *= p;
			}
		}
	}

	for (c = 3; c < M; c++) {
		//if (c % 10000 == 0) fprintf(stderr, "%d\n", c);
		cc = (c-1)/rad[c];
		if (rad[c-1] <= cc)
			s += c;
		if (cc < 6) continue;
		if (c % 2 == 0 && cc < 15) continue;
		if (c % 3 == 0 && cc < 10) continue;
		for (a = 2; a < c/2; a++) {
			b = c - a;
			if (rad[a] > cc || rad[b] > cc) continue;
			if ((rad[a] <= cc/rad[b]) && (gcd(a, b) == 1))
				s += c;
		}
	}

	printf("Ans: %d\n", s);
	return 0;
}

