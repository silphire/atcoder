a, b, c = map(int, input().split())
if c == 1:
    b -= 1
if a == b:
    print('Aoki')
elif a > b:
    print('Takahashi')
else:
    print('Aoki')