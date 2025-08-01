class GameOfString:
    def check_vowel(self, character):
        if character in 'aeiou':
            return True
        return False

    def min_length(self, a, b):
        len_a = len(a)
        len_b = len(b)
        if len_a == 0 or len_b == 0:
            return 0
        table = [[0] * (len_b + 1) for _ in range(len_a + 1)]
        for i in range(1, len_a + 1):
            for j in range(1, len_b + 1):
                if a[i - 1] == b[j - 1] and not self.check_vowel(a[i - 1]):
                    table[i][j] = 1 + table[i - 1][j - 1]
                else:
                    table[i][j] = max(table[i - 1][j], table[i][j - 1])
        return table[len_a][len_b]


if __name__ == "__main__":
    string_a, string_b = input().split()
    game_of_string_instance = GameOfString()
    print(game_of_string_instance.min_length(string_a, string_b))
