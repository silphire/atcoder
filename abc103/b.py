s = input().rstrip()
t = input().rstrip()

s = s + s
if t in s:
    print('Yes')
else:
    print('No')