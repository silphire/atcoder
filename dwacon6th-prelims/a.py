n = int(input())
ss = [None] * n
tt = [0] * n
for i in range(n):
    s, t = input().split()
    ss[i] = s
    tt[i] = int(t)
x = input()
i = ss.index(x)
print(sum(tt[i+1:]))