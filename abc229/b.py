a, b = input().rstrip().split()
a = list(reversed(a))
b = list(reversed(b))
for aa, bb in zip(a, b):
    if int(aa) + int(bb) >= 10:
        print('Hard')
        exit()
print('Easy')
