n = int(input())
aa = list(map(int, input().split()))
ans = 1
f = 0
p = None
for a in aa:
    if f == 0:
        if p is not None:
            if p > a:
                f = -1
            elif p < a:
                f = 1
    elif f == -1:
        if p < a:
            ans += 1
            f = 0
    elif f == 1:
        if p > a:
            ans += 1
            f = 0
    p = a
print(ans)