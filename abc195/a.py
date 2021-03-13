m, h = map(int, input().split())
print(['No', 'Yes'][int(h % m == 0)])