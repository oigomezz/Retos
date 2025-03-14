#include <bits/stdc++.h>
using namespace std;

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int n;
  cin >> n;
  string chats[1001];
  for (int i = 0; i < n; i++)
    getline(cin, chats[i]);

  int days[31] = {0};
  for (int i = 0; i < n; i++)
  {
    int weight = 0;
    if (chats[i][0] == 'G')
      weight = 2;
    else
      weight = 1;

    string word;
    stringstream lineStream(chats[i]);
    while (lineStream >> word)
    {
      if (word >= "1" && word <= "30")
      {
        int number;
        number = stoi(word);
        days[number] += weight;
      }
    }
  }

  int max = days[0], maxdate = 0;
  for (int i = 1; i < 31; i++)
  {
    if (max < days[i])
    {
      max = days[i];
      maxdate = i;
    }
  }

  int maxDays = 0;
  for (int i = 0; i < 31; i++)
  {
    if (max == days[i])
      maxDays++;
  }

  if (maxDays > 1)
    cout << "No Date";
  else if (maxdate == 19 || maxdate == 20)
    cout << "Date";
  else
    cout << "No Date";

  return 0;
}