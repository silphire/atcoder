n = int(input())
aa = list(map(int, input().split()))
seen = set()
ans = set()
for a in aa:
    if a in seen:
        continue
    seen.add(a)
    while a % 2 == 0:
        a //= 2
        seen.add(a)
    ans.add(a)
print(len(ans))