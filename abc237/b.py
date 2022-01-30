h, w = map(int, input().split())
aa = [
    list(map(int, input().split()))
    for _ in range(h)
]

for x in range(w):
    b = [aa[i][x] for i in range(h)]
    print(' '.join(map(str, b)))