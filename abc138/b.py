n = int(input())
aa = list(map(int, input().split()))
s = 0.0
for a in aa:
    s += 1 / a
print(1 / s)
