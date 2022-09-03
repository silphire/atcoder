s = list(map(int, list(input().rstrip())))
if s[0] == 1:
    print('No')
    exit()
t = [
    s[6],
    s[3],
    s[1] + s[7],
    s[0] + s[4],
    s[2] + s[8],
    s[5],
    s[9]
]

li = 7
ri = 0
for i in range(len(t)):
    if t[i]:
        li = i
        break
for i in range(len(t) - 1, -1, -1):
    if t[i]:
        ri = i
        break

if ri - li > 1 and not all(t[li+1:ri]):
    print('Yes')
else:
    print('No')