x = {c:i for i, c in enumerate(input().rstrip())}
n = int(input())
s = sorted([
    input().rstrip()
    for _ in range(n)
], key=lambda a: tuple([x[c] for c in a]))
for ss in s:
    print(ss)