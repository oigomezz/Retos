#include <cstdio>
#include <vector>
#define min_4(a, b, c, d) min((min(a, b)), (min(c, d)))

using namespace std;

int main()
{
  vector<int> min_num_of_summands(1e6 + 1, 0);
  min_num_of_summands[0] = 0, min_num_of_summands[1] = -1;
  // Primes
  min_num_of_summands[2] = min_num_of_summands[3] = 1;
  min_num_of_summands[5] = min_num_of_summands[7] = 1;

  min_num_of_summands[6] = min_num_of_summands[4] = 2;
  min_num_of_summands[8] = 2;

  for (int i = 9; i <= 1e6; i++)
    min_num_of_summands[i] = 1 + min_4(min_num_of_summands[i - 2], min_num_of_summands[i - 3],
                                       min_num_of_summands[i - 5], min_num_of_summands[i - 7]);

  int test_cases;
  scanf("%d", &test_cases);

  while (test_cases--)
  {
    int number;
    scanf("%d", &number);
    printf("%d\n", min_num_of_summands[number]);
  }

  return 0;
}