#include "bits/stdc++.h"
using namespace std;
const int MAX = 105;
string S[MAX];
bool A[1000005];

int main()
{
  int n, k, c;
  string a, b;
  vector<pair<int, string>>::iterator it;
  cin >> n >> k;

  for (int i = 0; i < n; ++i)
  {
    cin >> S[i];
  }
  sort(S, S + n);
  map<string, vector<pair<int, string>>> m;
  for (int i = 0; i < k; ++i)
  {
    cin >> a >> b >> c;
    bool flag = true;
    for (int j = 0; j < n; ++j)
      if (a == S[j])
      {
        flag = false;
        break;
      }

    m[a].push_back(make_pair(c, b));
  }
  for (int i = 0; i < n; ++i)
  {
    sort(m[S[i]].begin(), m[S[i]].end());
    memset(A, false, sizeof(A));
    cout << S[i] << endl;
    for (it = m[S[i]].begin(); it != m[S[i]].end(); ++it)
    {
      cout << it->second << ' ' << it->first << endl;
      A[it->first] = true;
    }
  }
  return 0;
}