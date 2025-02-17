#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <list>
#include <iomanip>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <complex>
#include <sstream>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <numeric>
#include <utility>
#include <functional>
#include <stdio.h>
#include <assert.h>
#include <memory.h>
#include <bitset>
#include <math.h>
#include <strings.h>

#define f first
#define s second
#define pb push_back
#define sz(a) (int)(a).size()
#define lp(i, a, n) for (int(i) = (a); (i) <= (int)(n); (i)++)
#define lpd(i, n, a) for (int(i) = (n); (i) >= (a); --(i))
#define mp make_pair
#define clr(a, b) memset(a, b, sizeof a)
#define all(v) (v).begin(), (v).end()
#define mod 1000000007
#define eps 1e-6
#define infi 1000000002
#define infll 4000000000000000005ll
#define MX 1000000
#define X real()
#define Y imag()
#define polar(r, t) ((r) * exp(point(0, (t))))
#define length(a) hypot((a).X, (a).Y)
#define angle(a) atan2((a).Y, (a).X)
#define vec(a, b) ((b) - (a))
#define dot(a, b) (conj(a) * (b)).X
#define cross(a, b) (conj(a) * (b)).Y
#define lengthsqr(a) dot(a, a)
#define reflect(V, M) (conj((V) / (M)) * (M))
#define normalize(a) ((a) / length(a))
#define ccw(a, b, c) cross(vec(a, b), vec(a, c)) > -eps
#define cosRule(a, b, c) (acos(((a) * (a) + (b) * (b) - (c) * (c)) / (2 * (a) * (b))))
#define cosDot(a, b) (acos(dot(a, b) / length(a) / length(b)))
#define EQ(a, b) (fabs((a) - (b)) <= eps)
#define NE(a, b) (fabs((a) - (b)) > eps)
#define LT(a, b) ((a) < (b) - eps)
#define GT(a, b) ((a) > (b) + eps)
#define LE(a, b) ((a) <= (b) + eps)
#define GE(a, b) ((a) >= (b) - eps)
#define mod1 100050001
#define mod2 100030001
#define base1 37
#define base2 31
#define que priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>>
#define rotate(v, t) ((v) * exp(point(0, t)))
#define rotateabout(v, t, a) (rotate(vec(a, v), t) + (a))
#define PI atan(1) * 4

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<vi> vvi;
typedef set<int> si;
typedef map<int, int> mii;
typedef map<ll, ll> mll;
typedef unordered_map<ll, ll> umll;
typedef complex<long double> point;
typedef pair<point, point> line;
typedef pair<double, point> Circle;

const int N = 100005;

int n, a[5][N];

char str[N];
ll tree[5][5][N];

void update(int i, int v, ll tree[])
{
  while (i <= n)
    tree[i] += v, i += i & -i;
}

ll query(int i, ll tree[])
{
  ll ret = 0;
  while (i > 0)
    ret += tree[i], i -= i & -i;
  return ret;
}

int main()
{

  scanf("%d", &n);
  lp(j, 0, 4) lp(i, 1, n) scanf("%d", &a[j][i]);
  scanf("%s", str + 1);

  int p[] = {0, 1, 2, 3, 4};
  lp(k, 0, 4) lp(j, 0, 4) lp(i, 1, n) if (str[i] - 'A' == k)
      update(i, a[j][i], tree[k][j]);

  int q;
  scanf("%d", &q);

  while (q--)
  {
    char ch;
    scanf(" %c%c", &ch, &ch);

    if (ch == 'e')
    {
      char x, y;
      scanf(" %c %c", &x, &y);
      swap(p[x - 'A'], p[y - 'A']);
    }
    else if (ch == 'c')
    {
      int x;
      char y;
      scanf("%d %c", &x, &y);
      lp(i, 0, 4) update(x, -a[i][x], tree[str[x] - 'A'][i]);
      lp(i, 0, 4) update(x, a[i][x], tree[y - 'A'][i]);
      str[x] = y;
    }
    else
    {
      int x, y;
      scanf("%d%d", &x, &y);
      ll ans = 0;
      lp(i, 0, 4) ans += query(y, tree[i][p[i]]) - query(x - 1, tree[i][p[i]]);
      printf("%lld\n", ans);
    }
  }

  return 0;
}