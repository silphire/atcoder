s = input().rstrip()
if len(s) == 3:
    s = ''.join(reversed(s))
print(s)