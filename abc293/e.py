a, x, m = map(int, input().split())

if a == 1:
    print(x % m)
    exit()
ans = pow(a, x, m * (a - 1)) - 1
ans = ans // (a - 1) % m
print(ans)