n = int(input())
tt = list(map(int, input().split()))

s = sum(tt)
m = int(input())
for i in range(m):
    p, x = map(int, input().split())
    print(s - tt[p - 1] + x)