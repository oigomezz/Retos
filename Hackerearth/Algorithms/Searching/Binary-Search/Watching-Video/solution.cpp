#include <bits/stdc++.h>
#define ll long long int
using namespace std;

int main()
{
  ll n, d;
  cin >> n >> d;
  set<int> s;
  map<int, int> m;
  ll l[n], ind = 0;
  for (int i = 0; i < n; i++)
  {
    cin >> l[i];
    if (i != 0)
      l[i] += l[i - 1];
  }
  int i = n - 1;
  for (; l[i] == l[n - 1];)
    i--;

  n = i + 1;
  for (int i = 0; i < n; i++)
    for (; ind <= i && l[i] < (i - ind + 1) * d;)
      ind++;

  cout << ind + 1;
}