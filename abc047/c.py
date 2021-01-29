n = 0
p = None
for c in input().rstrip():
    if p and p != c:
        n += 1
    p = c
print(n)