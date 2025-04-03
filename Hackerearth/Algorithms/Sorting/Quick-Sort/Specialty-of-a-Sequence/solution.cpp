#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int partition(vector<int> &arr, int low, int high)
{
  int pivot = arr[high];
  int i = (low - 1);
  for (int j = low; j <= high - 1; j++)
  {
    if (arr[j] < pivot)
    {
      i++;
      swap(arr[i], arr[j]);
    }
  }
  swap(arr[i + 1], arr[high]);
  return (i + 1);
}

void quickSort(vector<int> &arr, int low, int high)
{
  if (low < high)
  {
    int pi = partition(arr, low, high);
    quickSort(arr, low, pi - 1);
    quickSort(arr, pi + 1, high);
  }
}
int main()
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  int n, k;
  cin >> n >> k;
  vector<int> arr(n);
  for (int i = 0; i < n; i++)
    cin >> arr[i];

  quickSort(arr, 0, n - 1);
  int sum = 0;
  for (int i = 0; i < n; i++)
  {
    int count = 0;
    for (int j = i + 1; j < n && count < k; j++)
      if (arr[j] > arr[i])
        count++;
    if (count == k)
      sum += arr[i];
  }
  cout << sum << endl;
  return 0;
}