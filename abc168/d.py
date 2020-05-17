from collections import defaultdict

n, m = map(int, input().split())
e = []
es = defaultdict(set)
for i in range(m):
    ee = tuple(sorted(map(int, input().split())))
    e.append(ee)
    es[ee[0]].add(ee[1])
    es[ee[1]].add(ee[0])

path = [None] * (n + 1)
path[1] = 1
num = 0
nodes = {1}
while nodes:
    new_nodes = set()
    for nd in nodes:
        for e in es[nd]:
            if path[e] is None:
                path[e] = nd
                num += 1
                new_nodes.add(e)
    nodes = new_nodes
if num == n - 1:
    print("Yes")
    for i in range(2, n + 1):
        print(path[i])
else:
    print("No")
