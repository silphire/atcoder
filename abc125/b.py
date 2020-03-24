n = int(input())
vv = list(map(int, input().split()))
cc = list(map(int, input().split()))

z = 0
for i in range(n):
    if vv[i] > cc[i]:
        z += vv[i] - cc[i]
print(z)
