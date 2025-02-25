class Solution:
    def multiply(self, matrix_a, matrix_b):
        MOD = 1000000009
        result_matrix = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    result_matrix[i][j] = (
                        result_matrix[i][j] + matrix_a[i][k] * matrix_b[k][j] + MOD) % MOD

        for i in range(2):
            for j in range(2):
                matrix_a[i][j] = result_matrix[i][j]

    def unlucky_13(self, n):
        MOD = 1000000009
        result_matrix = [[1, 0], [0, 1]]
        transformation_matrix = [[0, -1], [1, 10]]
        while n:
            if n % 2:
                self.multiply(result_matrix, transformation_matrix)
            self.multiply(transformation_matrix, transformation_matrix)
            n //= 2
        return (result_matrix[0][0] + (result_matrix[1][0] * 10) % MOD + MOD) % MOD


if __name__ == "__main__":
    test_cases = int(input())
    for _ in range(test_cases):
        n = int(input())
        solution_instance = Solution()
        print(solution_instance.unlucky_13(n))
