n, m = map(int, input().split())
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))

cc = sorted(set(aa) & set(bb))
print(' '.join(map(str, cc)))