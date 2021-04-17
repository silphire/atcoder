n = int(input())
s = input().rstrip()

t = 'b'
m = 0
if s == t:
    print(0)
    exit()
while len(t) <= len(s):
    t = 'a' + t + 'c'
    m += 1
    if t == s:
        print(m)
        exit()
    
    t = 'c' + t + 'a'
    m += 1
    if t == s:
        print(m)
        exit()
    
    t = 'b' + t + 'b'
    m += 1
    if t == s:
        print(m)
        exit()
print(-1)