#include <bits/stdc++.h>
#include <bits/extc++.h>
using namespace __gnu_pbds;
#define SZ(X) ((int)(X).size())
#define ALL(X) (X).begin(), (X).end()
#define REP(I, N) for (int I = 0; I < (N); ++I)
#define REPP(I, A, B) for (int I = (A); I < (B); ++I)
#define RI(X) scanf("%d", &(X))
#define RII(X, Y) scanf("%d%d", &(X), &(Y))
#define RIII(X, Y, Z) scanf("%d%d%d", &(X), &(Y), &(Z))
#define DRI(X) \
  int(X);      \
  scanf("%d", &X)
#define DRII(X, Y) \
  int X, Y;        \
  scanf("%d%d", &X, &Y)
#define DRIII(X, Y, Z) \
  int X, Y, Z;         \
  scanf("%d%d%d", &X, &Y, &Z)
#define RS(X) scanf("%s", (X))
#define CASET           \
  int ___T, case_n = 1; \
  scanf("%d ", &___T);  \
  while (___T-- > 0)
#define MP make_pair
#define PB push_back
#define MS0(X) memset((X), 0, sizeof((X)))
#define MS1(X) memset((X), -1, sizeof((X)))
#define LEN(X) strlen(X)
#define PII pair<int, int>
#define VI vector<int>
#define VPII vector<pair<int, int>>
#define PLL pair<long long, long long>
#define VPLL vector<pair<long long, long long>>
#define F first
#define S second
typedef long long LL;
using namespace std;
const int MOD = 1e9 + 7;
const int SIZE = 1e6 + 10;
VPII e[SIZE];
typedef tree<pair<long double, int>, null_type, less<pair<long double, int>>, rb_tree_tag, tree_order_statistics_node_update> set_t;
set_t s;
double m_m;
LL num;
LL dp[SIZE];
LL qq, pp;
int h[SIZE];
void f(int x, int lt, long double v)
{
  int nn = s.order_of_key(MP(v - 1e-12, 0));
  num += SZ(s) - nn;
  if (nn != SZ(s))
  {
    int id = s.find_by_order(nn)->S;
    LL tmp_q = dp[x] - dp[id];
    LL tmp_p = h[x] - h[id];
    int gg = __gcd(tmp_p, tmp_q);
    tmp_q /= gg;
    tmp_p /= gg;
    if (tmp_q * pp > tmp_p * qq)
    {
      pp = tmp_p;
      qq = tmp_q;
    }
    REPP(j, 1, 10)
    {
      if (nn + j < SZ(s))
      {
        id = s.find_by_order(nn + j)->S;
        tmp_q = dp[x] - dp[id];
        tmp_p = h[x] - h[id];
        gg = __gcd(tmp_p, tmp_q);
        tmp_q /= gg;
        tmp_p /= gg;
        if (tmp_q * pp > tmp_p * qq)
        {
          pp = tmp_p;
          qq = tmp_q;
        }
      }
    }
  }
  s.insert(MP(v, x));
  REP(i, SZ(e[x]))
  {
    int y = e[x][i].F;
    if (y == lt)
      continue;
    h[y] = h[x] + 1;
    dp[y] = dp[x] + e[x][i].S;
    f(y, x, v + e[x][i].S - m_m);
  }
  s.erase(MP(v, x));
}
VPII ker;
bool compare(const PII &X, const PII &Y)
{
  return (LL)X.F * Y.S < (LL)X.S * Y.F;
}
int far[SIZE];
void spf(int x, int lt)
{
  int now = x;
  REP(k, 20)
  {
    if (now == 1)
      break;
    now = far[now];
    PII me = MP(dp[x] - dp[now], h[x] - h[now]);
    int gg = __gcd(me.F, me.S);
    me.F /= gg;
    me.S /= gg;
    ker.PB(me);
  }
  REP(i, SZ(e[x]))
  {
    int y = e[x][i].F;
    if (y == lt)
      continue;
    far[y] = x;
    dp[y] = dp[x] + e[x][i].S;
    h[y] = h[x] + 1;
    spf(y, x);
  }
}
void special(int n, int K)
{
  spf(1, 1);
  sort(ALL(ker), compare);
  printf("%d/%d\n", ker[K - 1].F, ker[K - 1].S);
}
int main()
{
  DRI(n);
  LL K;
  scanf("%lld", &K);
  int ma = 0;
  REPP(i, 1, n)
  {
    DRIII(x, y, v);
    e[x].PB(MP(y, v));
    e[y].PB(MP(x, v));
    ma = max(ma, v);
  }
  if (K <= 500)
  {
    special(n, K);
    return 0;
  }
  long double ll = 1, rr = ma + 1, lt;
  REP(tt, 50)
  {
    qq = 0;
    pp = 1;
    m_m = (ll + rr) * 0.5;
    num = 0;
    f(1, 1, 0);
    if (num == K)
      break;
    if (num < K)
      ll = m_m;
    else
    {
      rr = m_m;
      lt = m_m;
    }
  }
  if (num < K)
  {
    qq = 0;
    pp = 1;
    num = 0;
    m_m = lt;
    f(1, 1, 0);
  }
  printf("%lld/%lld\n", qq, pp);
  return 0;
}