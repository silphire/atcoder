d = int(input())
n = int(input())
cc = [0] * (d + 1)
for _ in range(n):
    l, r = map(int, input().split())
    cc[l - 1] += 1
    cc[r] -= 1
for i in range(1, d):
    cc[i] += cc[i - 1]
for i in range(d):
    print(cc[i])