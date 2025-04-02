#include <bits/stdc++.h>
using namespace std;
#define int long long
#define mod 1000000007

int power(int a, int n)
{
  int ans = 1;
  while (n)
  {
    if (n & 1)
      ans = (ans * a) % mod;

    a = (a * a) % mod;
    n = n >> 1;
  }
  return ans;
}

struct user_entry
{
  string name;
  int age;
  string hometown;
  string address;
};

struct redundant_entry
{
  int i;
  int j;
};

signed main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  int n;
  cin >> n;
  user_entry u[n];
  for (int i = 0; i < n; i++)
    cin >> u[i].name >> u[i].age >> u[i].hometown >> u[i].address;

  int k = 0;
  vector<struct redundant_entry> v;
  for (int i = 0; i < n; i++)
  {
    for (int j = i + 1; j < n; j++)
    {
      if (u[i].name == u[j].name || u[i].address == u[j].address || u[i].age == u[j].age || u[i].hometown == u[j].hometown)
      {
        k++;
        redundant_entry a;
        a.i = i;
        a.j = j;
        v.push_back(a);
      }
    }
  }
  cout << k << endl;
  for (int i = 0; i < v.size(); i++)
    cout << (v[i].i + 1) << ' ' << (v[i].j + 1) << endl;

  return 0;
}