aa = [
    list(map(int, input().split()))
    for _ in range(3)
]
col = [
    [0] * 3
    for _ in range(3)
]

def dfs(turn, pt, pa, r):
    global aa, col

    for y in range(3):
        f = True
        for x in range(3):
            if col[y][x] == 0 or col[y][x] != col[y][0]:
                f = False
                break
        if f:
            return 3 - turn
    for x in range(3):
        f = True
        for y in range(3):
            if col[y][x] == 0 or col[y][x] != col[0][x]:
                f = False
                break
        if f:
            return 3 - turn
    f = True
    for i in range(3):
        if col[i][i] == 0 or col[i][i] != col[0][0]:
            f = False
            break
    if f:
        return 3 - turn
    f = True
    for i in range(3):
        if col[i][2 - i] == 0 or col[i][2 - i] != col[0][2]:
            f = False
            break
    if f:
        return 3 - turn
        
    if r == 0:
        if pt > pa:
            return 1
        else:
            return 2
    for y in range(3):
        for x in range(3):
            if col[y][x] != 0:
                continue
            col[y][x] = turn
            if turn == 1:
                win = dfs(2, pt + aa[y][x], pa, r - 1)
            else:
                win = dfs(1, pt, pa + aa[y][x], r - 1)
            col[y][x] = 0
            if win == turn:
                return turn
    return 3 - turn

ans = dfs(1, 0, 0, 9)
if ans == 1:
    print('Takahashi')
else:
    print('Aoki')