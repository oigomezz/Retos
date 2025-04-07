#include <bits/stdc++.h>
using namespace std;
#define int long long
#define fr(i, a, b) for (int i = a; i < b; i++)
#define frr(i, a, b) for (int i = a; i >= b; i--)

void input(int *arr, int n) { fr(i, 0, n) cin >> arr[i]; }
void output(int *arr, int n) { fr(i, 0, n) cout << arr[i] << " "; }

int32_t main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int n, k;
  cin >> n >> k;
  int arr[n];
  input(arr, n);
  sort(arr, arr + n);
  int res = arr[n - 1] - arr[0];
  fr(i, 0, n - 1)
  {
    int minElement = min(arr[0] + k, arr[i + 1] - k);
    int maxElement = max(arr[i] + k, arr[n - 1] - k);
    res = min(res, maxElement - minElement);
  }
  cout << res << "\n";
}
