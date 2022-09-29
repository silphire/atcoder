s = input().rstrip()
oa = ord('a')
if len(s) == 26:
    used = [True] * 26
    for i in range(26):
        c = ord(s[25 - i]) - oa
        used[c] = False
        s = s[:-1]
        for i in range(c + 1, 26):
            if not used[i]:
                s += chr(i + oa)
                print(s)
                exit()
else:
    used = [False] * 26
    for c in s:
        used[ord(c) - oa] = True
    for i in range(26):
        if not used[i]:
            s += chr(i + oa)
            print(s)
            exit()
print(-1)