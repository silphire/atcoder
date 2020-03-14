a = []
for _ in range(3):
    a.append(list(map(int, input().split())))
n = int(input())

for _ in range(n):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if a[i][j] == b:
                a[i][j] = 0

for i in range(3):
    f = True
    for j in range(3):
        if a[i][j] != 0:
            f = False
            break
    if f:
        print("Yes")
        exit(0)
    
    f = True
    for j in range(3):
        if a[j][i] != 0:
            f = False
            break
    if f:
        print("Yes")
        exit(0)

f = True
for i in range(3):
    if a[i][i] != 0:
        f = False
        break
if f:
    print("Yes")
    exit(0)

f = True
for i in range(3):
    if a[i][2 - i] != 0:
        f = False
        break
if f:
    print("Yes")
    exit(0)

print("No")