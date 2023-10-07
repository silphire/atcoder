from collections import Counter

n = int(input())
ss = [
    input()
    for _ in range(n)
]
r = [(-Counter(list(s))['o'], i) for i, s in enumerate(ss)]
print(*map(lambda x: x[1] + 1, sorted(r)))