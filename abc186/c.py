n = int(input())
ans = 0
for x in range(1, n + 1):
    if '7' not in str(x) and '7' not in oct(x):
        ans += 1
print(ans)