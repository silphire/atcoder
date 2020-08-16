n, x = map(int, input().split())
m = [0] * n
for i in range(n):
    m[i] = int(input())

ans = n + (x - sum(m)) // min(m)
print(ans)