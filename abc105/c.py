n = int(input())

if n == 0:
    print(0)
    exit(0)

ans = []
while n != 0:
    ans.append(n % 2)
    n = - (n // 2)
print(''.join(map(str, reversed(ans))))