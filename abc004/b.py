aa = [
    input().rstrip().split(' ')
    for _ in range(4)
]
for a in reversed(aa):
    print(' '.join(reversed(a)))