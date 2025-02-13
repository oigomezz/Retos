import sys
import io
import time


class A5:
    def __init__(self):
        self.is_ = None
        self.out = None
        self.INPUT = ""
        self.inbuf = bytearray(1024)
        self.lenbuf = 0
        self.ptrbuf = 0
        self.es = None
        self.xord = None
        self.par = None
        self.ord = None
        self.dep = None
        self.pw = None
        self.g = None
        self.dw = None
        self.K = 0
        self.gct = 0
        self.cache = {}

        self.I = 1000000  # long equivalent

    def solve(self):
        n = self.ni()
        self.K = self.nl()
        from_arr = [0] * (n - 1)
        to_arr = [0] * (n - 1)
        w = [0] * (n - 1)
        for i in range(n - 1):
            from_arr[i] = self.ni() - 1
            to_arr[i] = self.ni() - 1
            w[i] = self.ni()
        if n > 100000:
            self.I = 501
        self.g = A5.packWU(n, from_arr, to_arr, w)
        pars = A5.parents(self.g, 0)
        self.par = pars[0]
        self.ord = pars[1]
        self.dep = pars[2]
        # pars[3] is dw in int[] but not used here since we use long dw separately
        self.pw = pars[4]
        self.dw = [0] * n
        for i in range(1, n):
            cur = self.ord[i]
            self.dw[cur] = self.dw[self.par[cur]] + self.pw[cur]
        rights = A5.makeRights(self.g, self.par, 0)
        self.xord = rights[0]
        iord = rights[1]
        right = rights[2]
        self.es = [0] * (n * 2)
        p = 0
        for i in range(n):
            # (long) n - iord[i] << 32 | i << 1 | 1;
            self.es[p] = ((n - iord[i]) << 32) | (i << 1) | 1
            p += 1
            # (long) n - right[iord[i]] << 32 | i << 1 | 0;
            self.es[p] = ((n - right[iord[i]]) << 32) | (i << 1) | 0
            p += 1
        self.es.sort()
        ret = self.bisearchRationalNumbers()
        self.out.write(str(ret[0]) + "/" + str(ret[1]) + "\n")

    @staticmethod
    def sortByPreorder(g, root):
        n = len(g)
        stack = [0] * n
        ord = [0] * n
        ved = [False] * n
        stack[0] = root
        p = 1
        r = 0
        ved[root] = True
        while p > 0:
            cur = stack[p - 1]
            ord[r] = cur
            r += 1
            p -= 1
            for e in g[cur]:
                if not ved[e[0]]:
                    ved[e[0]] = True
                    stack[p] = e[0]
                    p += 1
        return ord

    @staticmethod
    def makeRights(g, par, root):
        n = len(g)
        ord = A5.sortByPreorder(g, root)
        iord = [0] * n
        for i in range(n):
            iord[ord[i]] = i
        right = [0] * n
        for i in range(n - 1, 0, -1):
            if right[i] == 0:
                right[i] = i
            p_index = iord[par[ord[i]]]
            right[p_index] = max(right[p_index], right[i])
        return [ord, iord, right]

    def ok(self, num, den):
        n = len(self.g)
        if n > 100000:
            vsi = [0] * n
            vsmin = 0
            for i in range(n):
                vsi[i] = self.dw[i] * den - num * self.dep[i]
                vsmin = min(vsi[i], vsmin)
            for i in range(n):
                # vsi[i] = (vsi[i] - vsmin) << 20 | i;
                vsi[i] = ((vsi[i] - vsmin) << 20) | i
            vsi = A5.radixSort(vsi)
            u = -1
            vs = [0] * n
            for i in range(n):
                if i == 0 or (vsi[i] >> 20) != (vsi[i - 1] >> 20):
                    u += 1
                vs[int(vsi[i] & ((1 << 20) - 1))] = u
            hash_val = 0
            for i in range(n):
                hash_val = hash_val * 1000000009 + vs[i]
            if hash_val in self.cache:
                return self.cache[hash_val]
            self.gct += 1
            id_val = u
            ft = [0] * (id_val + 3)
            ct = 0
            p = 0
            for i in range(n - 1, -1, -1):
                cur = self.xord[i]
                while p < 2 * n and (n - (self.es[p] >> 32)) >= i:
                    ind = (self.es[p] & ((1 << 32) - 1)) >> 1
                    sg = 1 if (self.es[p] & 1) == 1 else -1
                    ct += A5.sumFenwick(ft, vs[ind] - 1) * sg
                    p += 1
                A5.addFenwick(ft, vs[cur], 1)
            self.cache[hash_val] = (ct < self.K)
            return ct < self.K
        else:
            vsi = [0] * n
            for i in range(n):
                # dw/dep > num/den
                vsi[i] = self.dw[i] * den - num * self.dep[i]
            vsi.sort()
            u = 0
            # Remove duplicates from vsi array and store the first u unique values in vsi[0:u]
            unique_vsi = []
            for i in range(n):
                if i == 0 or vsi[i] != vsi[i - 1]:
                    unique_vsi.append(vsi[i])
                    u += 1
            vs = [0] * n
            for i in range(n):
                # Python's binary search in built-in list using bisect
                # since unique_vsi is sorted, we use bisect_left
                import bisect
                vs[i] = bisect.bisect_left(
                    unique_vsi, self.dw[i] * den - num * self.dep[i])
            hash_val = 0
            for i in range(n):
                hash_val = hash_val * 1000000009 + vs[i]
            if hash_val in self.cache:
                return self.cache[hash_val]
            self.gct += 1
            id_val = u
            ft = [0] * (id_val + 3)
            ct = 0
            p = 0
            for i in range(n - 1, -1, -1):
                cur = self.xord[i]
                while p < 2 * n and (n - (self.es[p] >> 32)) >= i:
                    ind = (self.es[p] & ((1 << 32) - 1)) >> 1
                    sg = 1 if (self.es[p] & 1) == 1 else -1
                    ct += A5.sumFenwick(ft, vs[ind] - 1) * sg
                    p += 1
                A5.addFenwick(ft, vs[cur], 1)
            self.cache[hash_val] = (ct < self.K)
            return ct < self.K

    @staticmethod
    def radixSort(f):
        to = [0] * len(f)
        # First pass (lowest 16 bits)
        b = [0] * 65537
        for i in range(len(f)):
            b[1 + (f[i] & 0xffff)] += 1
        for i in range(1, 65537):
            b[i] += b[i - 1]
        for i in range(len(f)):
            idx = (f[i] & 0xffff)
            to[b[idx]] = f[i]
            b[idx] += 1
        d = f
        f = to
        to = d
        # Second pass (next 16 bits)
        b = [0] * 65537
        for i in range(len(f)):
            b[1 + ((f[i] >> 16) & 0xffff)] += 1
        for i in range(1, 65537):
            b[i] += b[i - 1]
        for i in range(len(f)):
            idx = (f[i] >> 16) & 0xffff
            to[b[idx]] = f[i]
            b[idx] += 1
        d = f
        f = to
        to = d
        # Third pass (next 16 bits)
        b = [0] * 65537
        for i in range(len(f)):
            b[1 + ((f[i] >> 32) & 0xffff)] += 1
        for i in range(1, 65537):
            b[i] += b[i - 1]
        for i in range(len(f)):
            idx = (f[i] >> 32) & 0xffff
            to[b[idx]] = f[i]
            b[idx] += 1
        d = f
        f = to
        to = d
        # Fourth pass (highest 16 bits)
        b = [0] * 65537
        for i in range(len(f)):
            b[1 + ((f[i] >> 48) & 0xffff)] += 1
        for i in range(1, 65537):
            b[i] += b[i - 1]
        for i in range(len(f)):
            idx = (f[i] >> 48) & 0xffff
            to[b[idx]] = f[i]
            b[idx] += 1
        d = f
        f = to
        to = d
        return f

    @staticmethod
    def sumFenwick(ft, i):
        summ = 0
        i += 1
        while i > 0:
            summ += ft[i]
            i -= i & -i
        return summ

    @staticmethod
    def addFenwick(ft, i, v):
        if v == 0 or i < 0:
            return
        n = len(ft)
        i += 1
        while i < n:
            ft[i] += v
            i += i & -i

    def bisearchRationalNumbers(self):
        bp = 0
        bq = 1
        p = 1
        q = 0
        dir_flag = False
        while q <= self.I:
            a = 1
            while True:
                if a > self.I:
                    return [p, q]
                # if (dir XOR (not ok(...)))
                # In Python, use ^ for boolean xor
                if (dir_flag ^ (not self.ok(a * p + bp, a * q + bq))):
                    low = a // 2
                    high = a
                    while high - low > 1:
                        ha = (high + low) // 2
                        if (dir_flag ^ self.ok(ha * p + bp, ha * q + bq)):
                            low = ha
                        else:
                            high = ha
                    np = low * p + bp
                    nq = low * q + bq
                    bp = p
                    bq = q
                    p = np
                    q = nq
                    break
                a *= 2
            dir_flag = not dir_flag
        return [p, q]

    @staticmethod
    def parents(g, root):
        n = len(g)
        par = [-1] * n
        dw = [0] * n
        pw = [0] * n
        dep = [0] * n
        q = [0] * n
        q[0] = root
        p_ptr = 0
        r = 1
        while p_ptr < r:
            cur = q[p_ptr]
            p_ptr += 1
            for nex in g[cur]:
                if par[cur] != nex[0]:
                    q[r] = nex[0]
                    r += 1
                    par[nex[0]] = cur
                    dep[nex[0]] = dep[cur] + 1
                    dw[nex[0]] = dw[cur] + nex[1]
                    pw[nex[0]] = nex[1]
        return [par, q, dep, dw, pw]

    @staticmethod
    def packWU(n, from_arr, to_arr, w):
        g = [None] * n
        p = [0] * n
        for f in from_arr:
            p[f] += 1
        for t in to_arr:
            p[t] += 1
        for i in range(n):
            g[i] = [[0, 0] for _ in range(p[i])]
        for i in range(len(from_arr)):
            p[from_arr[i]] -= 1
            g[from_arr[i]][p[from_arr[i]]][0] = to_arr[i]
            g[from_arr[i]][p[from_arr[i]]][1] = w[i]
            p[to_arr[i]] -= 1
            g[to_arr[i]][p[to_arr[i]]][0] = from_arr[i]
            g[to_arr[i]][p[to_arr[i]]][1] = w[i]
        return g

    def run(self):
        if self.INPUT == "":
            self.is_ = sys.stdin.buffer
        else:
            self.is_ = io.BytesIO(self.INPUT.encode())
        self.out = sys.stdout
        s = int(time.time() * 1000)
        self.solve()
        self.out.flush()
        if self.INPUT != "":
            A5.tr(str(int(time.time() * 1000) - s) + "ms")

    @staticmethod
    def tr(*o):
        sys.stdout.write(str(o) + "\n")

    def readByte(self):
        if self.lenbuf == -1:
            raise Exception("InputMismatchException")
        if self.ptrbuf >= self.lenbuf:
            self.ptrbuf = 0
            try:
                data = self.is_.read(1024)
            except Exception:
                raise Exception("InputMismatchException")
            if not data:
                self.lenbuf = -1
                return -1
            self.inbuf = bytearray(data)
            self.lenbuf = len(self.inbuf)
        ret = self.inbuf[self.ptrbuf]
        self.ptrbuf += 1
        return ret

    def ni(self):
        num = 0
        b = self.readByte()
        minus = False
        while b != -1 and not ((b >= ord('0') and b <= ord('9')) or b == ord('-')):
            b = self.readByte()
        if b == ord('-'):
            minus = True
            b = self.readByte()
        while True:
            if b >= ord('0') and b <= ord('9'):
                num = num * 10 + (b - ord('0'))
            else:
                return -num if minus else num
            b = self.readByte()

    def nl(self):
        num = 0
        b = self.readByte()
        minus = False
        while b != -1 and not ((b >= ord('0') and b <= ord('9')) or b == ord('-')):
            b = self.readByte()
        if b == ord('-'):
            minus = True
            b = self.readByte()
        while True:
            if b >= ord('0') and b <= ord('9'):
                num = num * 10 + (b - ord('0'))
            else:
                return -num if minus else num
            b = self.readByte()

    def getPtrbuf(self):
        return self.ptrbuf

    def setPtrbuf(self, ptrbuf):
        self.ptrbuf = ptrbuf


@staticmethod
def main():
    A5().run()


if __name__ == "__main__":
    A5().run()
