MOD = 10 ** 9 + 7
n = int(input())
aa = list(map(int, input().split()))

b = [0, 0, 0]
t = 1
for j, a in enumerate(aa):
    tt = 0
    for x in b:
        if x == a:
            tt += 1
    for i in range(3):
        if a == b[i]:
            b[i] = a + 1
            break
    t *= tt
    t %= MOD
print(t)