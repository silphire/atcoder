n, k, x = map(int, input().split())
aa = list(map(int, input().split()))
bb = aa[:k] + [x] + aa[k:]
print(*bb)