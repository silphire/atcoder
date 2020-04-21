n = int(input())
h = list(map(int, input().split()))

for i in range(n - 1, 0, -1):
    if i == n - 1:
        continue
    if h[i] - h[i + 1] == 1:
        h[i] -= 1
    elif h[i] - h[i + 1] > 1:
        print("No")
        exit(0)
print("Yes")
