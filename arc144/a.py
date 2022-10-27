n = int(input())
m = 2 * n
print(m)
if n % 4 == 0:
    print('4' * (n // 4))
else:
    print(f'{n % 4}{"4" * (n // 4)}')