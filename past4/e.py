import itertools

n = int(input())
s = tuple(input().rstrip())
r = tuple(reversed(s))

for x in itertools.permutations(s, n):
    if x == s or x == r:
        continue
    print(''.join(x))
    exit()
print('None')