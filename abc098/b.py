n = int(input())
s = input().rstrip()

ans = 0
for i in range(n):
    x = s[:i]
    y = s[i:]
    ans = max(ans, len(set(x) & set(y)))
print(ans)