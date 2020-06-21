n, k = map(int, input().split())
pp = tuple(map(int, input().split()))

print(sum(sorted(pp)[:k]))