#include <bits/stdc++.h>
using namespace std;

#define scan(x) scanf("%d", &x)

char tr[100000], res[100000];

int main()
{
  int t, i, j, len;
  cin >> t;
  while (t--)
  {
    scanf("%s %s", tr, res);
    len = strlen(res);
    sort(res, res + len);
    j = 0;
    for (i = 0; tr[i]; ++i)
      if (j < len && tr[i] > res[j])
        tr[i] = res[j++];

    printf("%s\n", tr);
  }

  return 0;
}