import sys

MAXT = 50
MAXL = 1000

keys = [
    "_0",
    ".,?!1",
    "abc2",
    "def3",
    "ghi4",
    "jkl5",
    "mno6",
    "pqrs7",
    "tuv8",
    "wxyz9"
]


def valid(s):
    return s in {'.', ',', '?', '!', '_'} or ('a' <= s <= 'z') or ('0' <= s <= '9')


def get_pos(c):
    for i in range(10):
        for j in range(len(keys[i])):
            if keys[i][j] == c:
                return i


def press(c, p):
    for i in range(len(keys[p])):
        if keys[p][i] == c:
            return i + 1


def main():
    T = int(input().strip())
    assert 0 < T <= MAXT
    for _ in range(T):
        S = input().strip()
        len_s = len(S)
        assert 0 < len_s <= MAXL

        ans = 0
        pos = 1
        for i in range(len_s):
            assert valid(S[i])
            newpos = get_pos(S[i])
            if newpos != pos:
                ans += 1
            pos = newpos
            ans += press(S[i], pos)
        print(ans)


if __name__ == "__main__":
    main()
