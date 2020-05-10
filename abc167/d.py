n, k = map(int, input().split())
a = list(map(lambda x: int(x) - 1, input().split()))

c = [None] * 200000
cc = set()
p = 0
st = 0
ed = 0
i = 0
while True:
    c[i] = p
    cc.add(p)
    i += 1
    p = a[p]
    if p in cc:
        st = c.index(p)
        ed = i
        break
if k < ed:
    print(c[k] + 1)
else:
    k -= st
    k %= ed - st
    print(c[st + k] + 1)