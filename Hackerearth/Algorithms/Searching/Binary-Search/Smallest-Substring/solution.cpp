#include <bits/stdc++.h>
using namespace std;

int SmallestSubString(string S)
{
  int n = (int)S.size();
  int left = 0, right = 0;
  set<int> s;
  for (auto x : S)
    s.insert(x);
  int target = (int)s.size();
  map<char, int> mp;
  int ans = n;
  while (right < n)
  {
    mp[S[right]]++;
    while (mp.size() == target)
    {
      ans = min(ans, right - left + 1);
      mp[S[left]]--;
      if (mp[S[left]] == 0)
        mp.erase(S[left]);
      left++;
    }
    right++;
  }
  return ans;
}

int main()
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  string S;
  cin >> S;
  int out_;
  out_ = SmallestSubString(S);
  cout << out_;
  return 0;
}