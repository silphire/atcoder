from collections import Counter
print(['No', 'Yes'][int(all([n % 2 == 0 for _, n in Counter(list(input().rstrip())).items()]))])