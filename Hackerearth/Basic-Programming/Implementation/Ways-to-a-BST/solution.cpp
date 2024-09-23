#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
const ll maxN = 1000;
const ll MOD = 1e9 + 7;
struct node {
  ll val, tot;
  node * lc, * rc;
};
ll fact[maxN];
node * init(ll val) {
  node * nd = (node * ) malloc(sizeof(node));
  nd -> val = val;
  nd -> lc = nd -> rc = NULL;
  return nd;
}
ll mulMod(ll a, ll b) {
  return ((a % MOD) * (b % MOD)) % MOD;
}
node * insert(node * r, ll val) {
  if (!r) {
    node * nd = init(val); //(node*)
    malloc(sizeof(node));
    return nd;
  }
  if (val <= (r -> val)) r -> lc = insert(r -> lc, val);
  else r -> rc = insert(r -> rc, val);
  return r;
}
ll update(node * r) {
  if (!r) return 0;
  r -> tot = 1 + update(r -> lc) + update(r -> rc);
  return (r -> tot);
}
ll power(ll a, ll b) {
  if (b == 0) return 1;
  ll ret = power(mulMod(a, a), b / 2) % MOD;
  if (b % 2) ret = mulMod(a, ret);
  return ret;
}
ll getInv(ll a) {
  return power(a, MOD - 2);
}
ll getCnt(node * r) {
  if (!r) return 1;
  ll lCnt, rCnt, ans, x, y;
  lCnt = getCnt(r -> lc);
  rCnt = getCnt(r -> rc);
  x = ((!(r -> lc)) ? 0 : ((r -> lc) -> tot));
  y = ((!(r -> rc)) ? 0 : ((r -> rc) -> tot));
  ans = mulMod(mulMod(getInv(fact[x]), getInv(fact[y])), mulMod(lCnt, rCnt));
  ans = mulMod(ans, fact[x + y]);
  return ans;
}
void preprocess() {
  ll i;
  fact[0] = 1;
  for (i = 1; i <= maxN; ++i) {
    fact[i] = mulMod(i, fact[i - 1]);
  }
}
int main() {
  ll t, n, m, i, j, ans, a;
  preprocess();
  scanf("%lld", & t);
  while (t--) {
    scanf("%lld", & n);
    ans = 0;
    node * root = NULL;
    for (i = 0; i < n; ++i) {
      scanf("%lld", & a);
      root = insert(root, a);
    }
    update(root);
    ans = getCnt(root);
    printf("%lld\n", ans);
  }
  return 0;
}