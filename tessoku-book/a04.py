n = int(input())
s = ''
while n > 0:
    s = str(n & 1) + s
    n >>= 1
s = ('0' * 10) + s
print(s[len(s) - 10:])