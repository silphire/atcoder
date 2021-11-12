s = input().rstrip()
n = len(s)

def f(p):
    global s, n
    r = ''
    i = p
    while i < n:
        c = s[i]
        if c == '(':
            x, i = f(i + 1)
            r += x + ''.join(reversed(x))
        elif c == ')':
            return r, i + 1
        else:
            r += c
            i += 1
    return r, i

a, i = f(0)
print(a)