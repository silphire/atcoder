n, d = map(int, input().split())
tt = list(map(int, input().split()))

for i in range(n - 1):
    if tt[i + 1] - tt[i] <= d:
        print(tt[i + 1])
        exit()
print(-1)