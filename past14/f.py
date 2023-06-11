n = int(input())
ss = set(map(int, input().split()))
q = int(input())

ans = len(ss)
for _ in range(q):
    m = int(input())
    tt = set(map(int, input().split()))
    x = 0
    for t in tt:
        if t not in ss:
            x += 1
    print(ans + x)