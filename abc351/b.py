n = int(input())
aa = [
    input()
    for _ in range(n)
]
bb = [
    input()
    for _ in range(n)
]
for i in range(n):
    if aa[i] != bb[i]:
        for j in range(n):
            if aa[i][j] != bb[i][j]:
                print(i + 1, j + 1)