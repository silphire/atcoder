n = int(input())
ss = [
    input()
    for _ in range(3)
]

x = 0
for i in range(n):
    a = len(set([ss[j][i] for j in range(3)]))
    x += [0, 0, 1, 2][a]
print(x)