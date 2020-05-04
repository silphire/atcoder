from collections import Counter
print(sorted(Counter(input().rstrip()).items(), key=lambda x: x[1])[-1][0])