n = int(input())
aa = [
    input().rstrip()
    for _ in range(n)
]
for i in range(n):
    for j in range(n):
        if i == j and aa[i][i] == '-':
            continue
        if aa[i][j] == 'W' and aa[j][i] == 'L':
            continue
        if aa[i][j] == 'L' and aa[j][i] == 'W':
            continue
        if aa[i][j] == 'D' and aa[j][i] == 'D':
            continue
        print('incorrect')
        exit()
print('correct')