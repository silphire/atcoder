n = int(input())
ss = list(map(int, input().split()))

aa = [0] * n
an = 0
for i in range(n):
    aa[i] = ss[i] - an
    an += aa[i]
print(*aa)