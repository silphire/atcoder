t = int(input())
n = int(input())
aa = [0] * (t + 2)
for _ in range(n):
    l, r = map(int, input().split())
    aa[l] += 1
    aa[r] -= 1
for i in range(t + 1):
    aa[i + 1] += aa[i]
for i in range(t):
    print(aa[i])