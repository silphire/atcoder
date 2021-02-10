n = int(input())
aa = list(map(int, input().split()))
av = sum(aa) // n
ans = 0
for a in aa:
    ans += (a - av) ** 2

av += 1
ans2 = 0
for a in aa:
    ans2 += (a - av) ** 2

print(min(ans, ans2))