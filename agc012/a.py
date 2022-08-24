n = int(input())
aa = list(map(int, input().split()))

print(sum(sorted(aa)[n::2]))