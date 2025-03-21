#include <bits/stdc++.h>
using namespace std;

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  int n, q, i;
  cin >> n >> q;
  string a, b;
  cin >> a;
  cin >> b;
  vector<int> v;
  int counta = 0, countb = 0;
  for (i = 0; i < n; i++)
  {
    if (b[i] == '1')
      countb++;
    if (a[i] == '1')
      counta++;
  }
  while (q--)
  {
    int k;
    cin >> k;
    if (b[k - 1] == '0')
    {
      b[k - 1] = '1';
      countb++;
    }

    if (countb >= counta)
      cout << "YES" << "\n";
    else
      cout << "NO" << "\n";
  }
}