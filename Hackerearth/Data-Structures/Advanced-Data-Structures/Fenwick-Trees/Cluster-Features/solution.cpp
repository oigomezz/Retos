#include <bits/stdc++.h>

using namespace std;
const int MAXX = 150005;
const int N = 20005;
int x[MAXX], y[MAXX], queryx1[MAXX], queryx2[MAXX], queryy1[MAXX], queryy2[MAXX];
enum borderState
{
  OPEN,
  POINT,
  CLOSE,
};

struct segmentBorder
{
  borderState state;
  int yd, yu, x, idx;
  bool operator<(const segmentBorder &s)
  {
    return x < s.x || (x == s.x && state < s.state);
  }
};

struct BIT
{
  int n;
  long long int ls, ss;
  BIT operator+(const BIT &a)
  {
    return {n + a.n, ls + a.ls, ss + a.ss};
  }

  BIT operator-(const BIT &a)
  {
    return {n - a.n, ls - a.ls, ss - a.ss};
  }
} B[N];

BIT ans[2][MAXX];

void updateBit(int idx, int val)
{
  long long int valss = val * 1LL * val;
  while (idx < N)
  {
    B[idx].n += 1;
    B[idx].ls += val;
    B[idx].ss += valss;
    idx += idx & -idx;
  }
}

BIT getBit(int idx)
{
  BIT ret = {0, 0LL, 0LL};
  while (idx > 0)
  {
    ret.n += B[idx].n;
    ret.ls += B[idx].ls;
    ret.ss += B[idx].ss;
    idx -= idx & -idx;
  }
  return ret;
}

BIT get(int l, int r)
{
  return getBit(r) - getBit(l - 1);
}

void solve(int p, int q, int turn)
{
  vector<segmentBorder> borders;
  for (int i = 0; i < p; i++)
  {
    borders.push_back({POINT, y[i], -1, x[i], -1});
  }

  for (int i = 0; i < q; i++)
  {
    segmentBorder left_border({OPEN, queryy1[i], queryy2[i], queryx1[i], i});
    segmentBorder right_border({CLOSE, queryy1[i], queryy2[i], queryx2[i], i});

    borders.push_back(left_border);
    borders.push_back(right_border);
  }

  sort(borders.begin(), borders.end());

  for (int i = 0; i < borders.size(); i++)
  {

    if (borders[i].state == POINT)
    {

      updateBit(borders[i].yd, borders[i].x);
    }
    else if (borders[i].state == OPEN)
    {
      BIT val = get(borders[i].yd, borders[i].yu);
      ans[turn][borders[i].idx] = ans[turn][borders[i].idx] - val;
    }
    else if (borders[i].state == CLOSE)
    {
      BIT val = get(borders[i].yd, borders[i].yu);
      ans[turn][borders[i].idx] = ans[turn][borders[i].idx] + val;
    }
  }
}

long long int magic(BIT t)
{
  unsigned long long int ret = t.n * 1ULL * t.ss - t.ls * 1ULL * t.ls;
  ret = ret * 3ULL;
  ret += t.ls;
  return ret;
}

int main()
{
  int p, q;
  cin >> p >> q;
  for (int i = 0; i < p; i++)
  {
    cin >> x[i] >> y[i];
  }
  for (int i = 0; i < q; i++)
  {
    cin >> queryx1[i] >> queryx2[i] >> queryy1[i] >> queryy2[i];
  }

  solve(p, q, 0);

  for (int i = 0; i < p; i++)
  {
    swap(x[i], y[i]);
  }

  for (int i = 0; i < q; i++)
  {
    swap(queryx1[i], queryy1[i]);
    swap(queryx2[i], queryy2[i]);
  }

  memset(B, 0, sizeof B);
  solve(p, q, 1);

  for (int i = 0; i < q; i++)
  {
    unsigned long long int val = magic(ans[0][i]) + magic(ans[1][i]);
    printf("%llu\n", val);
  }

  return 0;
}