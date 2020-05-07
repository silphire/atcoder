n = int(input())
p = list(map(int, input().split()))

x = 0
for i in range(n - 2):
    if p[i + 1] == sorted(p[i:i+3])[1]:
        x += 1
print(x)
