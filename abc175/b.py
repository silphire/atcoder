import itertools

n = int(input())
l = list(map(int, input().split()))

x = 0
for ls in itertools.combinations(l, 3):
    if len(set(ls)) != 3:
        continue
    if ls[0] + ls[1] > ls[2] and ls[1] + ls[2] > ls[0] and ls[0] + ls[2] > ls[1]:
        x += 1
print(x)