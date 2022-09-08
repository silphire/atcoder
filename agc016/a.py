s = list(input().rstrip())
s = [set([c]) for c in s]
x = 0
while s:
    u = s[0]
    for i in range(1, len(s)):
        u &= s[i]
    if u:
        print(x)
        exit()
    s = [s[i] | s[i + 1] for i in range(len(s) - 1)]
    x += 1
