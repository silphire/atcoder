a = int(input())
m = 0
for b in range(1, a):
    m = max(m, b * (a - b))
print(m)