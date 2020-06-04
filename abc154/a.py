s, t = input().rstrip().split()
a, b = map(int, input().split())
u = input().rstrip()

if s == u:
    a -= 1
else:
    b -= 1
print('{} {}'.format(a, b))