import itertools
print(''.join(sorted(itertools.product(input().rstrip(), repeat=2))[int(input()) - 1]))