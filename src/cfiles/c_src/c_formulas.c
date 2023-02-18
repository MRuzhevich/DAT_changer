#include <stdlib.h>
#include <math.h>
#include <stdint.h>

/* Returns a very crude approximation of Pi
   given a int: a number of iteration */
float pi_approx(int n)
{

    double i, x, y, sum = 0;

    for (i = 0; i < n; i++)
    {

        x = rand();
        y = rand();

        if (sqrt(x * x + y * y) < sqrt((double)RAND_MAX * RAND_MAX))
            sum++;
    }

    return 4 * (float)sum / (float)n;
}

uint64_t simple_sum(uint64_t a, uint64_t b)
{
    return a + b;
}