#include <bits/stdc++.h>
using namespace std;
using ll = int64_t;

inline int msb(ll x) { return 63 - __builtin_clzll(x); }

inline ll bitwise_AND(ll l, ll r)
{
    return msb(l) == msb(r) ? l & ~((1ll << (msb(l ^ r) + 1)) - 1) : 0;
}

inline ll solve(ll l, ll r, ll k)
{
    if (k == 1)
        return r;
    const ll m = 1ll << msb(r), u = m - 1, v = k - 1;
    if (r - l == v)
        return bitwise_AND(l, r);
    ll ans = 0;
    if (u - l >= v)
        ans = max(ans, bitwise_AND(u - v, u));
    if (r - m >= v)
        ans = max(ans, bitwise_AND(r - v, r));
    return ans;
}

int main()
{
    int Q;
    cin.tie(nullptr)->sync_with_stdio(false), cin >> Q;
    for (ll l, r, k; Q--; cout << solve(l, r, k) << '\n')
        cin >> l >> r >> k;
    return 0;
}