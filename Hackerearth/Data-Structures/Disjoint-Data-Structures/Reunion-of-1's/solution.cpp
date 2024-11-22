#include <bits/stdc++.h>
using namespace std;
int n, q, maxx, par[100005], len[100005];

int find(int x)
{
  if (x == par[x])
    return par[x];
  return par[x] = find(par[x]);
}

void unionset(int a, int b)
{
  int para = find(a), parb = find(b);
  if (para == parb)
    return;
  if (len[para] < len[parb])
  {
    par[para] = parb;
    len[parb] += len[para];
    maxx = max(maxx, len[parb]);
  }
  else
  {
    par[parb] = para;
    len[para] += len[parb];
    maxx = max(maxx, len[para]);
  }
}

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  cin >> n >> q;
  string s;
  cin >> s;
  s = "0" + s + "0";
  for (int i = 1; i <= n; i++)
  {
    if (s[i] == '1')
    {
      len[i] = 1;
      par[i] = i;
      maxx = 1;
    }
  }
  for (int i = 1; i <= n; i++)
  {
    if (s[i] == '1')
    {
      if (s[i - 1] == '1')
        unionset(i - 1, i);
    }
  }
  while (q--)
  {
    int type;
    cin >> type;
    if (type == 1)
      cout << maxx << endl;
    else
    {
      int ind;
      cin >> ind;
      if (s[ind] == '1')
        continue;
      s[ind] = '1';
      len[ind] = 1;
      par[ind] = ind;
      maxx = max(maxx, 1);
      if (s[ind - 1] == '1')
        unionset(ind - 1, ind);
      if (s[ind + 1] == '1')
        unionset(ind, ind + 1);
    }
  }
  return 0;
}