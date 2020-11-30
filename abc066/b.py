s = input().rstrip()

while len(s) > 0:
    s = s[:-2]
    x = s[:len(s) // 2]
    if x + x == s:
        print(len(s))
        exit()