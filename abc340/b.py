aa = []
q = int(input())
for _ in range(q):
    c, x = map(int, input().split())
    if c == 1:
        aa.append(x)
    else:
        print(aa[-x])