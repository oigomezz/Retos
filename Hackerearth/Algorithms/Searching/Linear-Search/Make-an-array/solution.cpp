#include <stdio.h>
#include <stdbool.h>
#include <malloc.h>
#include <stdlib.h>
int solve(int N, int *A)
{
  long long totalSum = 0;
  long long maxElement = 0;

  for (int i = 0; i < N; i++)
  {
    totalSum += A[i];
    if (A[i] > maxElement)
    {
      maxElement = A[i];
    }
  }

  if (totalSum % (N - 1) != 0)
  {
    return -1;
  }

  long long target = totalSum / (N - 1);

  if (maxElement > target)
  {
    return -1;
  }

  long long requiredMoves = 0;
  for (int i = 0; i < N; i++)
  {
    requiredMoves += (target - A[i]);
  }

  return requiredMoves == target ? target : -1;
}

int main()
{
  int T;
  scanf("%d", &T);
  for (int t_i = 0; t_i < T; t_i++)
  {
    int N;
    scanf("%d", &N);
    int i_A;
    int *A = (int *)malloc(sizeof(int) * (N));
    for (i_A = 0; i_A < N; i_A++)
      scanf("%d", &A[i_A]);

    int out_ = solve(N, A);
    printf("%d", out_);
    printf("\n");
  }
}