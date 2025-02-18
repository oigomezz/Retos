#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define INF 1e9 + 8

const int MAX = 2000005;

#define next nxt

char txt[MAX];
int iSA[MAX], SA[MAX];
int cnt[MAX], next[MAX];
bool bh[MAX], b2h[MAX];

bool smaller_first_char(int a, int b)
{
  return txt[a] < txt[b];
}

void suffixSort(int n)
{
  for (int i = 0; i < n; ++i)
  {
    SA[i] = i;
  }
  sort(SA, SA + n, smaller_first_char);

  for (int i = 0; i < n; ++i)
  {
    bh[i] = i == 0 || txt[SA[i]] != txt[SA[i - 1]];
    b2h[i] = false;
  }

  for (int h = 1; h < n; h <<= 1)
  {
    int buckets = 0;
    for (int i = 0, j; i < n; i = j)
    {
      j = i + 1;
      while (j < n && !bh[j])
        j++;
      next[i] = j;
      buckets++;
    }
    if (buckets == n)
      break;

    for (int i = 0; i < n; i = next[i])
    {
      cnt[i] = 0;
      for (int j = i; j < next[i]; ++j)
      {
        iSA[SA[j]] = i;
      }
    }

    cnt[iSA[n - h]]++;
    b2h[iSA[n - h]] = true;
    for (int i = 0; i < n; i = next[i])
    {
      for (int j = i; j < next[i]; ++j)
      {
        int s = SA[j] - h;
        if (s >= 0)
        {
          int head = iSA[s];
          iSA[s] = head + cnt[head]++;
          b2h[iSA[s]] = true;
        }
      }
      for (int j = i; j < next[i]; ++j)
      {
        int s = SA[j] - h;
        if (s >= 0 && b2h[iSA[s]])
        {
          for (int k = iSA[s] + 1; !bh[k] && b2h[k]; k++)
            b2h[k] = false;
        }
      }
    }
    for (int i = 0; i < n; ++i)
    {
      SA[iSA[i]] = i;
      bh[i] |= b2h[i];
    }
  }
  for (int i = 0; i < n; ++i)
  {
    iSA[SA[i]] = i;
  }
}

char *T = txt;
char s[MAX];
int n, m, h[MAX], ran[MAX];
vector<pair<string, int>> v;

pii tree[4 * MAX];

inline void merge(pii &p, pii &l, pii &r)
{
  p.fi = min(l.fi, r.fi);
  p.se = max(l.se, r.se);
}

void build(int node, int start, int end)
{
  if (start == end)
  {
    tree[node].fi = ran[h[SA[start]]];
    tree[node].se = ran[h[SA[start]]];
  }
  else
  {
    int mid = (start + end) >> 1;
    int left = node << 1;
    int right = left + 1;
    build(left, start, mid);
    build(right, mid + 1, end);
    merge(tree[node], tree[left], tree[right]);
  }
}

pii query(int node, int start, int end, int l, int r)
{
  if (l <= start and end <= r)
    return tree[node];
  if (end < l or r < start)
    return mp(INF, -1);
  int left = node << 1;
  int right = left + 1;
  int mid = (start + end) >> 1;
  pii p1 = query(left, start, mid, l, r);
  pii p2 = query(right, mid + 1, end, l, r);
  pii p;
  merge(p, p1, p2);
  return p;
}

pii stringMatching(char s[])
{
  int lo = 0, hi = n - 1, mid = lo;
  while (lo < hi)
  {
    mid = (lo + hi) >> 1;
    if (strncmp(T + SA[mid], s, m) >= 0)
      hi = mid;
    else
      lo = mid + 1;
  }
  if (strncmp(T + SA[lo], s, m) != 0)
    return {-1, -1};

  pii ans;

  ans.fi = lo;
  lo = 0;
  hi = n - 1, mid = lo;
  while (lo < hi)
  {
    mid = (lo + hi) >> 1;
    if (strncmp(T + SA[mid], s, m) > 0)
      hi = mid;
    else
      lo = mid + 1;
  }
  if (strncmp(T + SA[hi], s, m) != 0)
    hi--;
  ans.se = hi;
  return ans;
}

int main()
{
  int N, Q;
  scanf("%d%d", &N, &Q);
  int len = 0;
  for (int i = 0; i < N; ++i)
  {
    scanf("%s", s);
    strcat(T, s);
    strcat(T, "$");
    int k = 0;
    while (s[k] != '\0')
      k++, h[len++] = i;
    h[len++] = i;
    v.push_back(make_pair(s, i));
  }
  n = strlen(T);
  suffixSort(n);
  sort(v.begin(), v.end());
  for (int i = 0; i < N; ++i)
    ran[v[i].second] = i;
  build(1, 0, n - 1);

  pii pos;

  for (int i = 0; i < Q; ++i)
  {
    scanf("%s", s);
    m = strlen(s);
    pos = stringMatching(s);
    if (pos.fi != -1 and pos.se != -1)
    {
      pii ans = query(1, 0, n - 1, pos.fi, pos.se);
      printf("%d %d\n", v[ans.fi].se, v[ans.se].se);
    }
    else
    {
      printf("-1 -1\n");
    }
  }
  return 0;
}