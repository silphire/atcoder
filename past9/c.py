n = int(input())
ans = {}
for i in range(n):
    p, v = input().rstrip().split()
    if v == 'AC' and p not in ans:
        ans[p] = i + 1
for c, n in sorted(ans.items()):
    print(n)