from collections import Counter
s = input().rstrip()
c = Counter(s[i:i+2] for i in range(len(s) - 1))
print(sorted(c.most_common(), key=lambda x: (-x[1], x[0]))[0][0])