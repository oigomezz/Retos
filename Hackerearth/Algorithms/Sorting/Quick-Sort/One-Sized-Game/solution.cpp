#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define pp pair

vector<pp<ll, ll>> v;
int aa[100005];

void update(int inx)
{
  while (inx < 100005)
  {
    aa[inx] += 1;
    inx += inx & -inx;
  }
}

int getindex(int inx)
{
  int ans = 0;
  while (inx > 0)
  {
    ans += aa[inx];
    inx -= inx & -inx;
  }
  return ans;
}

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  int t;
  cin >> t;
  while (t--)
  {
    ll x;
    int n;
    cin >> n;
    v.clear();
    for (int i = 1; i <= n; i++)
      cin >> x, v.pb(mp(x, i));

    sort(v.begin(), v.end());

    int j = 0;
    ll sub = 0, previ = 0;
    bool won = false;
    while (j <= n - 1)
    {
      if (v[j].f >= sub)
      {
        if (j == n - 1)
          won = true;
        previ = v[j].s - getindex(v[j].s);

        ll mul = (v[j].f - sub) / previ;
        mul++;
        sub = sub + mul * previ;
      }
      update(v[j].s);
      j++;
    }

    if (!won)
      cout << "Kushagra\n";
    else
      cout << "Ladia\n";

    memset(aa, 0, sizeof(aa));
  }
  return 0;
}