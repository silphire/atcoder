n, m = map(int, input().split())
aa = list(sorted(map(int, input().split())))
bb = list(sorted(map(int, input().split())))

print(sorted(aa + list(map(lambda b: b + 1, bb)))[m - 1])