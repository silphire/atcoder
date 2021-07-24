ss = [
    input().rstrip()
    for _ in range(4)
]

if set(('H', '2B', '3B', 'HR')) == set(ss):
    print('Yes')
else:
    print('No')