#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

long long f[1000005];
long long ans[1000005];
long long arr[1000005];

void markMultiples(long long a)
{
    long long i = 2, num;
    while ((num = i * a) <= 1000005)
    {
        if (arr[num] == 0)
            arr[num] += a;
        ++i;
    }
}

void SieveOfEratosthenes()
{
    for (long long i = 2; i < 1000005; ++i)
    {
        if (arr[i] == 0)
        {
            arr[i] = (arr[i - 1] + i);
            markMultiples(i);
        }
        else
            arr[i] += arr[i - 1];
    }
}

int main()
{
    SieveOfEratosthenes();
    memset(f, 0, sizeof(f));
    memset(ans, 0, sizeof(ans));
    long long i = 0, j = 0;
    for (i = 1; i <= (1000002 / 2); i++)
    {
        for (j = i + i; j < 1000002; j += i)
        {
            f[j] += i;
        }
    }
    for (i = 2; i < 1000002; i++)
        ans[i] = ans[i - 1] + f[i];
    int t;
    scanf("%d", &t);
    while (t--)
    {
        long long n;
        scanf("%lld", &n);
        printf("%lld\n", (ans[n] + arr[n]) % n);
    }
    return 0;
}