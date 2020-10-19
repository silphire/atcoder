n, m = map(int, input().split())
la, ra = map(int, input().split())
for i in range(1, m):
    lm, rm = map(int, input().split())
    overlap = False
    if lm <= la <= rm and lm <= ra <= rm:
        continue
    if la <= lm <= ra:
        la = lm
        overlap = True
    if la <= rm <= ra:
        ra = rm
        overlap = True
    if not overlap:
        print(0)
        exit(0)

print(ra - la + 1)
