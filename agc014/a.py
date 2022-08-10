aa = tuple(map(int, input().split()))
v = set()
x = 0
while all(map(lambda a: a % 2 == 0, aa)):
    if aa in v or len(set(aa)) == 1:
        print(-1)
        exit()
    bb = [0] * 3
    for i in range(3):
        for j in range(3):
            if i != j:
                bb[j] += aa[i] // 2
    aa = tuple(bb)
    x += 1
print(x)