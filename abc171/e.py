n = int(input())
aa = tuple(map(int, input().split()))

v = aa[0]
for i in range(1, n):
    v ^= aa[i]
print(' '.join([str(v ^ a) for a in aa]))
