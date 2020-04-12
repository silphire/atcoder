import itertools

n = int(input())
s = input().rstrip()

colname = {'R': 0, 'G': 1, 'B': 2}
color = [[], [], []]
for i in range(n):
    ci = colname[s[i]]
    color[ci].append(i + 1)
color = sorted(color, key=lambda x: len(x))

color[2] = set(color[2])
nc2 = len(color[2])

x = 0
for r in color[0]:
    for g in color[1]:
        x += nc2
        if (r + r - g) in color[2]:
            x -= 1
        if (g + g - r) in color[2]:
            x -= 1
        c = r + g
        if c % 2 == 0 and (c // 2) in color[2]:
            x -= 1
print(x)