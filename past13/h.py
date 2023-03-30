from collections import Counter

d = int(input())
n = tuple(map(int, input()))
ctr = Counter(n)

x = 0
for d in n:
    ctr[d] -= 1
    for i in range(10):
        x += ctr[i] * abs(d - i)
print(x)