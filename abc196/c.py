n = int(input())
ans = 0
for x in range(1, 10 ** 6 + 1):
    s = str(x)
    if int(s + s) > n:
        break
    ans += 1
print(ans)