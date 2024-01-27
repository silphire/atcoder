from collections import Counter
n = int(input())
hist = Counter(map(int, input().split())).most_common()
if len(hist) < 8:
    print(0)
else:
    print(hist[-1][1])