n = int(input())
cc = list(map(int, input().split()))

minall = min(cc)
minodd = min(cc[::2])
decodd = 0
decall = 0
nodd = n // 2 + n % 2

def h():
    return [
        c - decall - decodd if i % 2 == 0 else c - decall
        for i, c in enumerate(cc)
    ]

ans = 0
q = int(input())
for i in range(q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        fodd = s[1] % 2 == 1
        x = cc[s[1] - 1] - decall
        if fodd:
            x -= decodd
        if x >= s[2]:
            cc[s[1] - 1] -= s[2]
            x -= s[2]
            if fodd:
                minodd = min(minodd, x)
                minall = min(minall, minodd)
            else:
                minall = min(minall, x)
            ans += s[2]
    elif s[0] == 2:
        if minodd >= s[1]:
            decodd += s[1]
            minodd -= s[1]
            minall = min(minall, minodd)
            ans += s[1] * nodd
    else:
        if minall >= s[1]:
            decall += s[1]
            minall -= s[1]
            minodd -= s[1]
            ans += s[1] * n
    # print(f'{ans} {minall} {decall} {minodd} {decodd} {h()}')
print(ans)