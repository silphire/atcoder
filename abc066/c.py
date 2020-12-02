n = int(input())
aa = tuple(map(int, input().split()))
bb = [0] * n

x = n // 2
s = 1 if n % 2 == 0 else -1
for i in range(1, n + 1):
    bb[x + s * (i // 2)] = aa[i - 1]
    s *= -1
print(' '.join(map(str, bb)))