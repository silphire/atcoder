n = int(input())
s = input().rstrip()

for i in range(n):
    if s[i] == '1':
        if i % 2 == 0:
            print('Takahashi')
        else:
            print('Aoki')
        exit()