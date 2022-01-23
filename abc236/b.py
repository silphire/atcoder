n = int(input())
aa = list(map(int, input().split()))
print(4 * n * (n + 1) // 2 - sum(aa))
