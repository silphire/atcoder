l, r = map(int, input().split())
s = input().rstrip()

print(s[:l-1] + ''.join(reversed(s[l-1:r])) + s[r:])