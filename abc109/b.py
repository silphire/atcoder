n = int(input())
pw = None
s = set()
ans = 'Yes'
for _ in range(n):
    w = input().rstrip()
    if pw is not None:
        if w[0] != pw[-1] or w in s:
            ans = 'No'
    pw = w
    s.add(w)
print(ans)