n = int(input())
s = [
    input().rstrip()
    for _ in range(2)
]
MOD = 1000000007

if s[0][0] == s[1][0]:
    ans = 3
    i = 1
    p = 0
else:
    ans = 6
    i = 2
    p = 1

while i < n:
    if s[0][i] == s[1][i]:
        if p == 0:
            ans *= 2
        else:
            ans *= 1
        p = 0
        i += 1
    else:
        if p == 0:
            ans *= 2
        else:
            ans *= 3
        p = 1
        i += 2
    ans %= MOD

print(ans)