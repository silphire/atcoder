n = int(input())
aa = list(map(int, input().split()))
bb = [0] * (n + 1)
for i in range(n):
    bb[i + 1] = bb[i] + aa[i]

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    w = (bb[r] - bb[l - 1])
    l = r - l + 1 - w
    if w > l:
        print('win')
    elif w < l:
        print('lose')
    else:
        print('draw')