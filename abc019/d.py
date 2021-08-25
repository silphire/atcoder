import sys

n = int(input())

a = 0
maxx = 0
for x in range(2, n + 1):
    print(f'? 1 {x}')
    sys.stdout.flush()
    b = int(input())
    if a < b:
        a = b
        maxx = x

ans = 0
for x in range(1, n + 1):
    if x == maxx:
        continue
    print(f'? {maxx} {x}')
    sys.stdout.flush()
    ans = max(ans, int(input()))

print(f'! {ans}')