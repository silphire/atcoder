n = int(input())
s = input()
r = ''
for i in range(len(s)):
    c = ord(s[i]) - ord('A') + n
    c = c % 26
    c = chr(c + ord('A'))
    r += c
print(r)

