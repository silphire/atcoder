n, q = map(int, input().split())
aa = [
    list(map(int, input().split()))
    for _ in range(n)
]
for _ in range(q):
    s, t = map(int, input().split())
    print(aa[s - 1][t])