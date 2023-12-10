n, s, k = map(int, input().split())
x = 0
for i in range(n):
    p, q = map(int, input().split())
    x += p * q
if x < s:
    x += k
print(x)