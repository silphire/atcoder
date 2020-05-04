import re

s = input().rstrip()

def solve(s):
    pass

r = re.compile(r'\([a-z]*\)')
while True:
    m = r.search(s)
    if not m:
        break

    ss = s[m.start()+1:m.end()-1]
    s = s[:m.start()] + ss + ''.join(reversed(ss)) + s[m.end():]

print(s)
exit(0)