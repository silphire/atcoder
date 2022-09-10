n = int(input())
pp = list(map(int, input().split()))
cnt = [0] * n

for i, p in enumerate(pp):
    for j in range(-1, 2):
        x = (p - i + j + n) % n
        cnt[x] += 1

print(max(cnt))