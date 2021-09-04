n = int(input())
pp = list(map(int, input().split()))

qq = [None] * n
for i in range(n):
    qq[pp[i] - 1] = i + 1
print(' '.join(map(str, qq)))