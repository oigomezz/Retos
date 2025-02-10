#include <bits/stdc++.h>
using namespace std;
#define int long long
#define all(x) x.begin(), x.end()
int st[1 << 18] = {};
void update(int pos, int val, int id = 1, int l = 1, int r = 1 << 17)
{
  if (pos < l || pos > r)
    return;
  if (l == r)
  {
    st[id] = val;
    return;
  }
  int mid = (l + r) >> 1;
  update(pos, val, id << 1, l, mid);
  update(pos, val, id << 1 | 1, mid + 1, r);
  st[id] = max(st[id << 1], st[id << 1 | 1]);
}
void find_left(int &res, int pos, int k, int id = 1, int l = 1, int r = 1 << 17)
{
  if (l > pos)
    return;
  if (res != -1)
    return;
  if (l == r)
  {
    if (st[id] >= k)
      res = l;
    return;
  }
  int mid = (l + r) >> 1;
  if (st[id << 1 | 1] >= k)
    find_left(res, pos, k, id << 1 | 1, mid + 1, r);
  if (st[id << 1] >= k)
    find_left(res, pos, k, id << 1, l, mid);
}
void find_right(int &res, int pos, int k, int id = 1, int l = 1, int r = 1 << 17)
{
  if (r < pos)
    return;
  if (res != -1)
    return;
  if (l == r)
  {
    if (st[id] >= k)
      res = l;
    return;
  }
  int mid = (l + r) >> 1;
  if (st[id << 1] >= k)
    find_right(res, pos, k, id << 1, l, mid);
  if (st[id << 1 | 1] >= k)
    find_right(res, pos, k, id << 1 | 1, mid + 1, r);
}
int32_t main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  int n;
  cin >> n;
  vector<pair<int, int>> u(n);
  vector<int> cc;
  for (auto &[id, sz] : u)
    cin >> id >> sz, cc.push_back(id);
  int nq;
  cin >> nq;
  vector<pair<int, int>> q(nq);
  for (auto &[pref, min_sz] : q)
    cin >> pref >> min_sz, cc.push_back(pref);
  sort(all(cc));
  cc.erase(unique(all(cc)), cc.end());
  auto get_pos = [&](int val)
  {
    return lower_bound(all(cc), val) - cc.begin() + 1;
  };
  for (auto &[id, sz] : u)
    id = get_pos(id);
  for (auto &[pref, min_sz] : q)
    pref = get_pos(pref);
  for (auto [id, sz] : u)
    update(id, sz);
  sort(all(u));
  auto get_val = [&](int id)
  {
    return lower_bound(all(u), make_pair(id, 0LL))->second;
  };
  for (auto [pref, min_sz] : q)
  {

    int l = -1, r = -1;
    find_left(l, pref, min_sz);
    find_right(r, pref, min_sz);
    if (l == -1)
    {
      if (r == -1)
        cout << -1 << ' ';
      else
      {
        cout << cc[r - 1] << ' ';
        // update(r, 0);
      }
    }
    else
    {
      if (r == -1)
      {
        cout << cc[l - 1] << ' ';
        // update(l, 0);
      }
      else
      {

        if (abs(cc[l - 1] - cc[pref - 1]) <= abs(cc[r - 1] - cc[pref - 1]))
        {
          cout << cc[l - 1] << ' ';
          // update(l, 0);
        }
        else
        {
          cout << cc[r - 1] << ' ';
          // update(r, 0);
        }
      }
    }
  }
  return 0;
}