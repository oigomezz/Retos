#include <bits/stdc++.h>
using namespace std;
int main()
{
  int num, queries;
  cin >> num >> queries;
  vector<pair<int, int>> question(num);
  for (int i = 0; i < num; i++)
  {
    int time;
    cin >> time;
    question[i].second = time;
  }

  for (int i = 0; i < num; i++)
  {
    int score;
    cin >> score;
    question[i].first = score;
  }
  sort(question.begin(), question.end());
  reverse(question.begin(), question.end());

  while (queries--)
  {
    int query;
    cin >> query;
    int ans = 0;
    for (int i = 0; i < query; i++)
      ans += question[i].second;
    cout << ans << endl;
  }
  return 0;
}