n, l = map(int, input().split())

s = [None] * n
for i in range(n):
    s[i] = input().rstrip()
print(''.join(sorted(s)))