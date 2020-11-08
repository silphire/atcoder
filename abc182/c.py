n = input().rstrip()
nn = len(n)

ans = -1
for b in range(1, 2 ** nn):
    bb = b
    t = ''
    i = 0
    while bb > 0:
        if bb % 2 == 1:
            t += n[i]
        bb //= 2
        i += 1
    if int(t) % 3 == 0:
        ans = max(ans, len(t))
if ans == -1:
    print(-1)
else:
    print(nn - ans)