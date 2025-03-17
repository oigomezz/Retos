class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False
        self.ctr = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s):
        curr = self.root
        curr.ctr += 1
        for c in s:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
            curr.ctr += 1
        curr.end = True

    def find(self, k):
        curr = self.root
        res = 0
        for pos in range(11):
            done = True
            for d in range(10):
                child = curr.child.get(str(d), TrieNode())
                total = pow(10, 10 - pos)
                count = total - child.ctr
                if k >= count:
                    k -= count
                else:
                    res = 10 * res + d
                    curr = child
                    done = False
                    break
            if done:
                break
        return res


def padstr(x): return "{:011}".format(x)


trie = Trie()
q = int(input())
for _ in range(q):
    qtype, val = map(int, input().split())
    if qtype == 1:
        x = val
        trie.insert(padstr(x))
    if qtype == 2:
        k = val
        print(trie.find(k))
