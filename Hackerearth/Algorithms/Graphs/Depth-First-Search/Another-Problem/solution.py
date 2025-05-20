class TestClass:
    n = 0
    adj = []
    vis = []
    V = []

    @staticmethod
    def check(string_array, index_i, index_j):
        m = len(string_array[index_i])
        for k in range(4):
            if string_array[index_i][m - 4 + k] != string_array[index_j][k]:
                return False
        return True

    @staticmethod
    def dfs(node, current_path):
        if len(current_path) == TestClass.n:
            TestClass.V.append(list(current_path))
            return
        for neighbor in TestClass.adj[node]:
            if not TestClass.vis[neighbor]:
                TestClass.vis[neighbor] = True
                current_path.append(neighbor)
                TestClass.dfs(neighbor, current_path)
                TestClass.vis[neighbor] = False
                current_path.pop()

    @staticmethod
    def main():
        TestClass.n = int(input())
        string_array = [input() for _ in range(TestClass.n)]

        TestClass.adj = [[] for _ in range(TestClass.n)]
        TestClass.vis = [False] * TestClass.n

        # Building the directed graph based on overlapping constraints
        for i in range(TestClass.n):
            for j in range(TestClass.n):
                if i == j:
                    continue
                if TestClass.check(string_array, i, j):
                    TestClass.adj[i].append(j)

        current_path = []
        for i in range(TestClass.n):
            TestClass.vis[i] = True
            current_path.append(i)
            TestClass.dfs(i, current_path)
            TestClass.vis[i] = False
            current_path.pop()

        result_set = set()

        # Append chunks to reconstruct the original message
        for vec in TestClass.V:
            reconstructed_string = string_array[vec[0]]
            for i in range(1, TestClass.n):
                reconstructed_string += string_array[vec[i]][4:]
            result_set.add(reconstructed_string)

        for result in sorted(result_set):
            print(result)


if __name__ == "__main__":
    TestClass.main()
