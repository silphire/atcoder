n = int(input())
pp = list(map(int, input().split()))
rr = {}
for i, p in enumerate(pp):
    rr[p] = i
q = int(input())
for _ in range(q):
    a, b = map(int, input().split())
    if rr[a] < rr[b]:
        print(a)
    else:
        print(b)