n, k = map(int, input().split())
print('\n'.join(sorted([input() for _ in range(n)][:k])))