#include <bits/stdc++.h>
#include <string>
#include <vector>
using namespace std;

typedef long long int ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef vector<vii> vvii;

#define INF 1e18
#define MOD 1000000007
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define loop(i, n) for (ll i = 0; i < n; i++)
#define leep(i, n) for (ll i = 1; i <= n; i++)

const int maxn = 1e5 + 6;
ll n, m, d;
ll a[maxn], pos[maxn], res[maxn], BIT[maxn];

struct Query
{
  int l, r, pos;
  bool operator<(const Query &q2)
  {
    return r < q2.r;
  }
};
vector<Query> Q(maxn);

void update(int ind)
{
  while (ind <= n)
  {
    BIT[ind]++;
    ind += ind & (-ind);
  }
}

ll query(ll ind)
{
  ll sum = 0;
  while (ind > 0)
  {
    sum += BIT[ind];
    ind -= ind & (-ind);
  }
  return sum;
}

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> n >> m >> d;

  for (int i = 1; i <= n; i++)
  {
    cin >> a[i];
    pos[a[i]] = i;
  }

  for (int i = 0; i < m; i++)
  {
    cin >> Q[i].l >> Q[i].r;
    Q[i].pos = i;
  }

  sort(Q.begin(), Q.begin() + m);
  int k = 0;
  for (int i = 1; i <= n; i++)
  {

    for (int j = max(1LL, a[i] - d); j <= min(n, a[i] + d); j++)
    {
      if (pos[j] <= i)
        update(pos[j]);
    }

    while (k < m && Q[k].r == i)
    {
      res[Q[k].pos] = query(i) - query(Q[k].l - 1);
      k++;
    }
  }

  for (int i = 0; i < m; i++)
  {
    cout << res[i] << "\n";
  }

  return 0;
}