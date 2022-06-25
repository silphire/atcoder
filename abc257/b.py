n, k, q = map(int, input().split())
aa = list(map(int, input().split()))
ll = list(map(int, input().split()))

for i in range(q):
    p = ll[i] - 1
    if p == k - 1:
        if aa[p] < n:
            aa[p] += 1
    else:
        if aa[p + 1] - aa[p] > 1:
            aa[p] += 1
print(*aa)