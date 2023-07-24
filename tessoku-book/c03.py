d = int(input())
aa = [0] * d
for i in range(d):
    aa[i] = aa[i - 1] + int(input())
q = int(input())
for _ in range(q):
    s, t = map(int, input().split())
    s -= 1
    t -= 1
    if aa[s] > aa[t]:
        print(s + 1)
    elif aa[s] < aa[t]:
        print(t + 1)
    else:
        print('Same')
