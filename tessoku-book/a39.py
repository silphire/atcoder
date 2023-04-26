n = int(input())
lr = sorted([
    tuple(map(int, input().split()))
    for _ in range(n)
], key=lambda x: x[1])
x = 0
ans = 0
for (l, r) in lr:
    if x <= l:
        x = r
        ans += 1
print(ans)