#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Function to compute the final position of each ant after t seconds
int getFinalPosition(int p, int d, int t, int n)
{
  // Compute the movement
  int newPosition = (p - 1 + d * t) % n;
  // Handle negative wrapping
  if (newPosition < 0)
    newPosition += n;
  return newPosition + 1; // Convert back to 1-based position
}

int main()
{
  int n, m, t;
  cin >> n >> m >> t;

  vector<int> finalPositions;
  for (int i = 0; i < m; i++)
  {
    int position, direction;
    cin >> position >> direction;
    finalPositions.push_back(getFinalPosition(position, direction, t, n));
  }

  // Sort the final positions in ascending order
  sort(finalPositions.begin(), finalPositions.end());

  // Output final positions
  for (int pos : finalPositions)
    cout << pos << " ";
  cout << endl;

  return 0;
}