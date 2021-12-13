n, k = map(int, input().split())
aa = [0] * n
bb = [0] * n
cc = [0] * n
for i in range(n):
    aa[i], bb[i], cc[i] = map(int, input().split())

ng = 0
ok = 10 ** 20
while ok - ng > 1:
    mid = (ok + ng) // 2
    cnt = 0
    for i in range(n):
        if mid < bb[i]:
            continue
        x = (mid - bb[i]) // cc[i] + 1
        cnt += min(x, aa[i])
    if k <= cnt:
        ok = mid
    else:
        ng = mid
print(ok)
