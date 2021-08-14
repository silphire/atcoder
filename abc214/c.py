n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
f = True
while f:
    f = False
    for i in range(n):
        nt = t[i - 1] + s[i - 1]
        if t[i] > nt:
            f = True
            t[i] = nt
for i in range(n):
    print(t[i])