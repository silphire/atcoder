ss = [
    input().rstrip()
    for _ in range(10)
]
for y in range(10):
    if '#' in ss[y]:
        a = y + 1
        c = ss[y].find('#') + 1
        d = ss[y].rfind('#') + 1
        break
for y in range(9, -1, -1):
    if '#' in ss[y]:
        b = y + 1
        break
print(a, b)
print(c, d)