n, m = map(int, input().split())
ss = [
    input().rstrip()
    for _ in range(n)
]
ss.append("")
tt = {
    input().rstrip()
    for _ in range(m)
}

x = sum(map(len, ss)) + n - 1
if not (3 <= x <= 16):
    print(-1)
    exit()
nb = 16 - x

ff = [True] * n
def dfs(arr, nb):
    global ff, tt
    fe = True
    for i in range(n):
        if ff[i]:
            fe = False
            ff[i] = False
            dfs(arr + (i, ), nb)
            ff[i] = True
    if fe:
        s = '_'.join([ss[a] for a in arr])
        if s not in tt:
            print(s)
            exit()
        return
    else:
        if nb > 0 and arr:
            dfs(arr + (n, ), nb - 1)

dfs((), nb)
print(-1)