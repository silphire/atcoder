x = int(input())
ans = 1000 * (x // 500)
ans += 5 * ((x % 500) // 5)
print(ans)