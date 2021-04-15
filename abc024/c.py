n, d, k = map(int, input().split())
l = [0] * d
r = [0] * d
for i in range(d):
    l[i], r[i] = map(int, input().split())
for i in range(k):
    s, t = map(int, input().split())
    ans = 0
    p = s
    for j in range(d):
        if l[j] <= p <= r[j]:
            if s < t:
                p = r[j]
            else:
                p = l[j]
        if s < t and p >= t:
            ans = j
            break
        elif s > t and p <= t:
            ans = j
            break
    print(ans + 1)