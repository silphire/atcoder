s = input()
ans = []
pos = {}
d = 0
for i, c in enumerate(s):
    if c == '(':
        pos[d] = i
        d += 1
    else:
        d -= 1
        ans.append((pos[d] + 1, i + 1))

for a in ans:
    print(*a)