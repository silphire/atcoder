class BinaryIndexedTree(object):
    """
    Fenwick Tree
    """
    def __init__(self, size: int):
        assert size > 0
        self.size = size + 1
        self.arr = [0] * self.size

    def add(self, pos: int, val: int) -> None:
        assert 0 < pos <= self.size

        p = pos
        while p < self.size:
            self.arr[p] += val
            p += p & -p

    def sum(self, pos: int) -> int:
        assert 0 <= pos <= self.size

        ans = 0
        p = pos
        while p > 0:
            ans += self.arr[p]
            p -= p & -p
        return ans

    def sum_range(self, left: int, right: int) -> int:
        assert 0 < left <= self.size
        assert 0 < right <= self.size
        assert left < right

        return self.sum(right - 1) - self.sum(left - 1)

    def get(self, pos: int) -> int:
        assert 0 < pos <= self.size
        return self.sum_range(pos, pos + 1)

def inversion_number(arr):
    """
    転倒数
    arr: [1, ..., n] が入っているリスト
    """
    n = len(arr)
    bit = BinaryIndexedTree(n + 1)
    r = 0
    for i, a in enumerate(arr):
        r += i - bit.sum(a)
        bit.add(a, 1)
    return r

n = int(input())
aa = list(map(int, input().split()))

print(inversion_number(aa))