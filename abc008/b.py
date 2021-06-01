from collections import Counter
n = int(input())
print(Counter([input() for _ in range(n)]).most_common()[0][0])