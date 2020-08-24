a, b, k = map(int, input().split())
ans = set()
for i in range(k):
    if a + i <= b:
        ans.add(a + i)
    if b - i >= a:
        ans.add(b - i)
for x in sorted(ans):
    print(x)