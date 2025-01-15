#include <bits/stdc++.h>
using namespace std;

int main()
{
	ios::sync_with_stdio(false), cin.tie(0);

	int n, m;
	cin >> n >> m;

	vector<vector<int>> grid(n, vector<int>(m));
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			cin >> grid[i][j];

	vector<vector<vector<int>>> pref(30, vector<vector<int>>(n, vector<int>(m)));
	for (int bit = 0; bit < 30; bit++)
	{

		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				if (grid[i][j] & (1 << bit))
					++pref[bit][i][j];

		for (int i = 1; i < n; i++)
			pref[bit][i][0] += pref[bit][i - 1][0];
		for (int i = 1; i < m; i++)
			pref[bit][0][i] += pref[bit][0][i - 1];
		for (int i = 1; i < n; i++)
			for (int j = 1; j < m; j++)
				pref[bit][i][j] += pref[bit][i][j - 1] +
													 pref[bit][i - 1][j] - pref[bit][i - 1][j - 1];
	}

	int q;
	cin >> q;
	while (q--)
	{
		int x1, y1, x2, y2;
		cin >> x1 >> y1 >> x2 >> y2;
		--x1;
		--y1;
		--x2;
		--y2;

		auto query = [&](int bit)
		{
			int cur = pref[bit][x2][y2];
			if (x1)
				cur -= pref[bit][x1 - 1][y2];
			if (y1)
				cur -= pref[bit][x2][y1 - 1];
			if (x1 && y1)
				cur += pref[bit][x1 - 1][y1 - 1];
			return cur;
		};

		int res = 0;
		for (int bit = 0; bit < 30; bit++)
			if (query(bit))
				res |= (1 << bit);

		cout << res << '\n';
	}
	return 0;
}