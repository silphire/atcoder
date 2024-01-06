n = int(input())
ss = []
for x in range(n + 1):
    for y in range(n + 1):
        for z in range(n + 1):
            if x + y + z > n:
                break
            ss.append((x, y, z))
for s in sorted(ss):
    print(*s)