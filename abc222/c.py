n, m = map(int, input().split())
aa = [
    list(input().rstrip())
    for _ in range(2 * n)
]

win = [(0, i) for i in range(2 * n)]
for r in range(m):
    for i in range(n):
        x = win[i * 2][1]
        y = win[i * 2 + 1][1]
        if aa[x][r] == 'G' and aa[y][r] == 'C' or aa[x][r] == 'C' and aa[y][r] == 'P' or aa[x][r] == 'P' and aa[y][r] == 'G':
            win[i * 2] = (win[i * 2][0] - 1, win[i * 2][1])
        if aa[y][r] == 'G' and aa[x][r] == 'C' or aa[y][r] == 'C' and aa[x][r] == 'P' or aa[y][r] == 'P' and aa[x][r] == 'G':
            win[i * 2 + 1] = (win[i * 2 + 1][0] - 1, win[i * 2 + 1][1])
    win = sorted(win)
for _, x in win:
    print(x + 1)