s = input().rstrip()
t = input().rstrip()
if len(s) <= len(t) and t[:len(s)] == s:
    print('Yes')
else:
    print('No')