n = int(input())
t, a = map(int, input().split())
hh = tuple(map(int, input().split()))

ans = 0
for i in range(1, n):
    if abs(t - hh[ans] * 0.006 - a) > abs(t - hh[i] * 0.006 - a):
        ans = i
print(ans + 1)
