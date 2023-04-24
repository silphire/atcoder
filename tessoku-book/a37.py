n, m, b = map(int, input().split())
aa = list(map(int, input().split()))
cc = list(map(int, input().split()))
print(m * sum(aa) + n * sum(cc) + n * m * b)