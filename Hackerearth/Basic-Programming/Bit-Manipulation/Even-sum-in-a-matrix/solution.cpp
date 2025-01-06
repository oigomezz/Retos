#include <bits/stdc++.h>

using namespace std;
int n, m;
int sum[2002][2002], a[2002][2002];
bitset<2002> bt[2002];
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> a[i][j];
            sum[i + 1][j + 1] = a[i][j] % 2;
        }
    }
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            sum[i][j] += sum[i][j - 1];
        }
    }
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            sum[i][j] += sum[i - 1][j];
            sum[i][j] %= 2;
            bt[i][j] = sum[i][j];
        }
    }
    long long sol = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j <= n; j++)
        {
            int c = (bt[i] ^ bt[j]).count();
            int d = m + 1 - c;
            sol += c * 1ll * (c - 1) / 2;
            sol += d * 1ll * (d - 1) / 2;
        }
    }
    cout << sol << endl;
}