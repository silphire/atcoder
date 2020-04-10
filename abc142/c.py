n = int(input())
aa = list(map(int, input().split()))
aaa = sorted([(aa[i], i + 1) for i in range(n)])
print(' '.join(map(str, [a[1] for a in aaa])))