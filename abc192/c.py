import sys

sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7
input = sys.stdin.readline

n, k = map(int, input().split())

a = n
for i in range(k):
    g2 = int(''.join(sorted(list(str(a)))))
    g1 = int(''.join(sorted(list(str(a)), reverse=True)))
    a = g1 - g2
print(a)
