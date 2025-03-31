#include <bits/stdc++.h>

using namespace std;

int vaccine[100000 + 10];
int patient[100000 + 10];

int main()
{
  ios::sync_with_stdio(false);
  cin.tie(0); // decrease the time of cin,, cout
  int n;
  cin >> n;
  for (int i = 0; i < n; i++)
    cin >> vaccine[i];
  for (int i = 0; i < n; i++)
    cin >> patient[i];

  sort(patient, patient + n); // sort the vaccine in ascending order
  sort(vaccine, vaccine + n); // sort the midichlorians count in ascending order

  for (int i = 0; i < n; i++)
  {
    if (vaccine[i] <= patient[i])
    { // if at least one patient can't be rescued, print No
      cout << "No";
      return 0;
    }
  }
  cout << "Yes";

  return 0;
}