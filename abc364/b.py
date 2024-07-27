h, w = map(int, input().split())
si, sj = map(int, input().split())
cc = [input() for _ in range(h)]
x = input()

si -= 1
sj -= 1
for a in x:
    if a == 'L' and sj - 1 >= 0 and cc[si][sj - 1] == '.':
        sj -= 1
    elif a == 'R' and sj + 1 < w and cc[si][sj + 1] == '.':
        sj += 1
    elif a == 'U' and si - 1 >= 0 and cc[si - 1][sj] == '.':
        si -= 1
    elif a == 'D' and si + 1 < h and cc[si + 1][sj] == '.':
        si += 1
print(si + 1, sj + 1)