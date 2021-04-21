n = int(input())
a, b = map(int, input().split())
k = int(input())
p = list(map(int, input().split()))

if len(set([a, b] + p)) == len(p) + 2:
    print('YES')
else:
    print('NO')