import itertools
print(sorted(sum(x) for x in itertools.combinations(map(int, input().split()), 3))[-3])