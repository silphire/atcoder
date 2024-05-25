n, t = map(int, input().split())
aa = list(map(int, input().split()))

row = [n] * n
col = [n] * n
dia = [n] * n

for i, a in enumerate(aa):
    r = (a - 1) // n
    c = (a - 1) %  n
    row[r] -= 1
    col[c] -= 1
    if r == c:
        dia[0] -= 1
    if r + c == n - 1:
        dia[1] -= 1

    if row[r] == 0 or col[c] == 0 or dia[0] == 0 or dia[1] == 0:
        print(i + 1)
        exit()
print(-1)