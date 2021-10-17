n = int(input())
aa = [0] * n
bb = [0] * n
cc = [0] * n
for i in range(n):
    a, b = map(int, input().split())
    aa[i] = a
    bb[i] = b
    cc[i] = a / b

s = sum(cc) / 2
i = 0
ans = 0
while i < n:
    if s - cc[i] < 0:
        break
    s -= cc[i]
    ans += aa[i]
    i += 1
ans += s * bb[i]
print(ans)