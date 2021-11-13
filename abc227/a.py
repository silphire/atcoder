n, k, a = map(int, input().split())
for i in range(k):
    a += 1
    if a > n:
        a = 1
a -= 1
if a == 0:
    a = n
print(a)