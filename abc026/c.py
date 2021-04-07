n = int(input())
b = [0] * n
for i in range(1, n):
    b[i] = int(input()) - 1
s = [1] * n
maxs = [0] * n
mins = [float('inf')] * n
for i in range(n - 1, 0, -1):
    if maxs[i] == 0:
        s = 1
    else:
        s = maxs[i] + mins[i] + 1
    maxs[b[i]] = max(maxs[b[i]], s)
    mins[b[i]] = min(mins[b[i]], s)
print(maxs[0] + mins[0] + 1)