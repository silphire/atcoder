n, m = map(int, input().split())
x, y = map(int, input().split())
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))

i = 0
j = 0
t = 0
ans = 0
while i < n and j < m:
    if ans % 2 == 0:
        if aa[i] < t:
            i += 1
        else:
            t = aa[i] + x
            ans += 1
    else:
        if bb[j] < t:
            j += 1
        else:
            t = bb[j] + y
            ans += 1
print(ans // 2)