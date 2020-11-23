import sys
sys.setrecursionlimit(200000)


n = int(input())
s = input().rstrip()

def skip_fox(p):
    global n
    global s
    pp = p

    t = 'fox'
    p += 1
    x = 1
    while x < 3:
        if p >= n:
            return pp
        if s[p] == t[x]:
            x += 1
            p += 1
            continue
        elif s[p] == 'f':
            prp = p
            p = skip_fox(p)
            if prp == p:
                return pp
        else:
            return pp
    return p

ans = 0
i = 0
while i < n:
    # print(f'{i} {ans}')
    if s[i] == 'f':
        pi = i
        i = skip_fox(i)
        if i >= n:
            break
        if pi < i:
            continue
    ans += 1
    i += 1
print(ans)