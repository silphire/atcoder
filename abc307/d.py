import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
s = input()

def dfs(p):
    r = ''
    i = p
    while i < n:
        if s[i] == '(':
            rr, i = dfs(i + 1)
            r += rr
        elif s[i] == ')' and p > 0:
            return '', i + 1
        else:
            r += s[i]
            i += 1
    if p == 0:
        return r, n
    else:
        return '(' + r, n

print(dfs(0)[0])