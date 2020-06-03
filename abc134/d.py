n = int(input())
aa = tuple(map(int, input().split()))

balls = set()
for i in range(n, 0, -1):
    r = aa[i - 1]
    
    x = 0
    for j in range(i, n + 1, i):
        if j in balls:
            x += 1
    if x % 2 != r:
        balls.add(i)
print(len(balls))
if balls:
    print(' '.join(map(str, balls)))