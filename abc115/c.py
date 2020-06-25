n, k = map(int, input().split())
hh = [0] * n
for i in range(n):
    hh[i] = int(input())

diff = float('inf')
hh = sorted(hh)
for i in range(n - k + 1):
    diff = min(diff, hh[i + k - 1] - hh[i])
print(diff)