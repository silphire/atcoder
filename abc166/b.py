n, k = map(int, input().split())
a = set()
for i in range(k):
    input()
    a = a | set(map(int, input().split()))
ans = set(range(1, n + 1)) - a
print(len(ans))