n, m = map(int, input().split())
ss = [
    input()
    for _ in range(n)
]

for yy in range(n):
    for xx in range(m):
        f = 0
        for y in range(3):
            for x in range(3):
                ax = xx + x
                ay = yy + y
                if not (0 <= ax < m and 0 <= ay < n):
                    f = 1
                    break
                if ss[ay][ax] == '.':
                    f = 2
                    break

                ax = xx + x + 6
                ay = yy + y + 6
                if not (0 <= ax < m and 0 <= ay < n):
                    f = 3
                    break
                if ss[ay][ax] == '.':
                    f = 4
                    break
            if f:
                break
        
        for i in range(4):
            ay = yy + 3
            ax = xx + i
            if not (0 <= ax < m and 0 <= ay < n):
                f = 5
                break
            if ss[ay][ax] == '#':
                f = 6
                break

            ay = yy + i
            ax = xx + 3
            if not (0 <= ax < m and 0 <= ay < n):
                f = 7
                break
            if ss[ay][ax] == '#':
                f = 8
                break

            ay = yy + 5
            ax = xx + i + 5
            if not (0 <= ax < m and 0 <= ay < n):
                f = 9
                break
            if ss[ay][ax] == '#':
                f = 10
                break

            ay = yy + i + 5
            ax = xx + 5
            if not (0 <= ax < m and 0 <= ay < n):
                f = 11
                break
            if ss[ay][ax] == '#':
                f = 12
                break
        if not f:
            print(f'{yy + 1} {xx + 1}')
