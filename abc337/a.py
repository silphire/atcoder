n = int(input())
xx = yy = 0
for _ in range(n):
    x, y = map(int, input().split())
    xx += x
    yy += y
if xx > yy:
    print('Takahashi')
elif xx < yy:
    print('Aoki')
else:
    print('Draw')