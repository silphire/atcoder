n = int(input())
aa = list(map(int, input().split()))

ans = 0
for a in aa:
    while a % 2 == 0 or a % 3 == 2:
        ans += 1
        a -= 1
print(ans)