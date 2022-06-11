r, c = map(int, input().split())
aa = [
    list(map(int, input().split()))
    for _ in range(2)
]
print(aa[r - 1][c - 1])