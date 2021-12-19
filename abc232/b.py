s = input().rstrip()
t = input().rstrip()
x = ord(t[0]) - ord(s[0])
if x < 0:
    x += 26
oa = ord('a')
ss = ''.join([chr((ord(c) - oa + x) % 26 + oa) for c in s])
if ss == t:
    print('Yes')
else:
    print('No')