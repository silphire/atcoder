n = int(input())
aa = list(map(int, input().split()))

N = 2 * 10 ** 5
acc = [0] * (N + 2)
for a in aa:
    acc[a] += 1
for i in range(1, N + 2):
    acc[i] += acc[i - 1]

ans = 0
for i in range(n):
    ans += acc[aa[i] - 1] * (n - acc[aa[i]])
print(ans)
