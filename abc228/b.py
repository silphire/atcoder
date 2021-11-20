n, x = map(int, input().split())
aa = list(map(int, input().split()))
ans = set()
while x not in ans:
    ans.add(x)
    x = aa[x - 1]
print(len(ans))