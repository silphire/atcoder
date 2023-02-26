n = int(input())
s = input()

st = set([(0, 0)])
x = 0
y = 0
for c in s:
    if c == 'R':
        x += 1
    elif c == 'L':
        x -= 1
    elif c == 'U':
        y += 1
    else:
        y -= 1
    if (x, y) in st:
        print('Yes')
        exit()
    st.add((x, y))
print('No')