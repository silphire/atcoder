t = {'W': 0, 'B': 1, 'R': 2}
n, c = input().split()
n = int(n)
sc = sum(map(lambda x: t[x], list(input()))) % 3
print(['No', 'Yes'][int(sc == t[c])])