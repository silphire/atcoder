import itertools

n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

x = sorted(itertools.permutations(list(range(1, n + 1))))
a = None
b = None
for i in range(len(x)):
    if p == x[i]:
        a = i
    if q == x[i]:
        b = i
    if a is not None and b is not None:
        break
print(abs(a - b))
