n = int(input())
a = [0] + list(map(int, input().split()))

ans = []
for i in range(1, n + 1):
    m = 1
    x = a[i]
    while x != i:
        x = a[x]
        m += 1
    ans.append(m)

print(' '.join(map(str, ans)))