n, k = map(int, input().split())
aa = set(map(lambda x: int(x) - 1, input().split()))

sk = []
for i in range(n):
    sk.append(i)
    if i not in aa:
        sk.append(i)

if k % 2 == 0:
    ans = 0
    for i in range(0, 2 * n - k, 2):
        ans += sk[i + 1] - sk[i]
    print(ans)
    exit()
else:
    la = [0]
    for i in range(0, 2 * n - k - 2, 2):
        la.append(la[-1] + sk[i + 1] - sk[i])
    ra = [0]
    for i in range(2 * n - k - 2, 0, -2):
        ra.append(ra[-1] + sk[i + 1] - sk[i])
    ans = float('inf')
    na = len(la)
    for i in range(na):
        ans = min(ans, la[i] + ra[-i - 1])
    print(ans)