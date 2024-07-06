from typing import Callable

class SegmentTree(object):
    """
    セグメント木
    """

    def __init__(self, arr: list[int], e: int, op: Callable[[int, int], int]):
        """
            arr: 初期値
            e: 単位元
            op: 二項演算
        """
        n = len(arr)
        self.p2 = 1 << n.bit_length()
        if self.p2 < n:
            self.p2 += 1

        self.n = n
        self.e = e
        self.op = op

        self.buf = [e] * (self.p2 * 2)
        for i in range(n):
            self.buf[self.p2 + i] = arr[i]
        for i in range(self.p2 - 1, -1, -1):
            self.buf[i] = op(self.buf[2 * i], self.buf[2 * i + 1])

    def set(self, i: int, x: int) -> None:
        """ i の位置を x に置き換える
        """
        assert 0 <= i < self.n

        i += self.p2
        self.buf[i] = x
        while i > 1:
            self.buf[i >> 1] = self.op(self.buf[i], self.buf[i ^ 1])
            i >>= 1

    def get(self, p: int, q: int) -> int:
        """ [p, q) に op を適用した結果を返す
        """
        assert 0 <= p <= self.n
        assert 0 <= q <= self.n
        assert p < q

        x = self.e

        p += self.p2
        q += self.p2
        while p < q:
            if p & 1:
                x = self.op(x, self.buf[p])
                p += 1
            if q & 1:
                x = self.op(x, self.buf[q - 1])
            p >>= 1
            q >>= 1

        return x

import sys

n, k = map(int, input().split())
aa = list(sorted(map(int, input().split())))

minseg = SegmentTree(aa, sys.maxsize, min)
maxseg = SegmentTree(aa, 0, max)

ans = sys.maxsize
for i in range(k + 1):
    ma = maxseg.get(i, i + n - k)
    mi = minseg.get(i, i + n - k)
    ans = min(ans, ma - mi)
print(ans)