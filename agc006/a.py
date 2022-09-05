n = int(input())
s = input().rstrip()
t = input().rstrip()

x = 0
for i in range(n):
    ss = s[len(s)-1-i:]
    tt = t[:i+1]
    if ss == tt:
        x = i + 1
print(len(s) + len(t) - x)