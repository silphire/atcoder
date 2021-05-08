n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = set(range(1, 1001))
for i in range(n):
    ans = ans & set(range(a[i], b[i] + 1))
print(len(ans))