n = int(input())
d = {}
for i in range(n):
    s, t = input().rstrip().split()
    if s not in d:
        d[s] = (-int(t), i + 1)
print(sorted(d.values())[0][1])
