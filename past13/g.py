n = int(input())
aa = list(map(int, input().split()))

r = float('-inf')
s = 0
for a in aa:
    s = max(s + a, a)
    r = max(r, s)
print(r)