n = int(input())
pp = [0, 0] + list(map(int, input().split()))
x = 0
while n > 0:
    n = pp[n]
    x += 1
print(x - 1)