import sys
sys.setrecursionlimit(20000)

s = input().rstrip()
n = len(s)
w = ['dream', 'dreamer', 'erase', 'eraser']
nw = [len(w[i]) for i in range(len(w))]

def dfs(start):
    global s
    global n
    global w
    global nw

    if start >= n:
        print('YES')
        exit()
    for i in range(4):
        if s.startswith(w[i], start):
            dfs(start + nw[i])

dfs(0)
print('NO')