n = int(input())
aa = list(map(int, input().split()))
pos = []
cnt = [0] * n
for i, a in enumerate(aa):
    cnt[a - 1] += 1
    if cnt[a - 1] == 2:
        pos.append((i, a))
pos = [a for (i, a) in sorted(pos)]
print(*pos)