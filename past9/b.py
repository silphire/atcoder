n = int(input())
ans = 0
for _ in range(n):
    a, b = map(int, input().split())
    c = b - a
    c %= 100
    ans += c // 50
    c %= 10
    ans += c // 5
print(ans)