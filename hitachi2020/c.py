global aa, bb

es = []
n = int(input())
for i in range(1, n):
    a, b = map(int, input().split())
    es.append((min(a, b), max(a, b)))
es = sorted(es)

threes = set()
for i in range(1, n + 1):
    visited = {i}
    cands = [i]
    for j in range(3):
        new_cands = []
        for c in cands:
            for e in es:
                if c == e[0] and e[1] not in visited:
                    new_cands.append(e[1])
                    visited.add(e[1])
                elif c == e[1] and e[0] not in visited:
                    new_cands.append(e[0])
                    visited.add(e[0])
        cands = new_cands
    for c in cands:
        threes.add((min(i, c), max(i, c)))

print(threes)
results = [0] * n
print(results)
