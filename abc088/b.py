n = int(input())
aa = list(sorted(map(int, input().split())))
print(abs(sum(aa[::2]) - sum(aa[1::2])))