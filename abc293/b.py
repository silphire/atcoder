n = int(input())
aa = list(map(int, input().split()))
f = [False] * n
for i in range(n):
    if not f[i]:
        f[aa[i] - 1] = True
ans = [i + 1 for i in range(n) if not f[i]]
print(len(ans))
print(*ans)