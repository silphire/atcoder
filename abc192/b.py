import sys

sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7
input = sys.stdin.readline

s = input().rstrip()
f = True
for i in range(len(s)):
    if i % 2 == 0:
        f = f and s[i].islower()
    else:
        f = f and s[i].isupper()
print(['No', 'Yes'][int(f)])