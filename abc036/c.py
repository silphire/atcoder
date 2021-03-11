n = int(input())
a = [0] * n
for i in range(n):
    a[i] = int(input())
index = sorted(set(a))
index = {x: i for i, x in enumerate(sorted(set(a)))}
for aa in a:
    print(index[aa])