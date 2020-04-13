n, k, q = map(int, input().split())
win = [0] * n
for _ in range(q):
    win[int(input()) - 1] += 1

for i in range(n):
    if k - q + win[i] > 0:
        print("Yes")
    else:
        print("No")