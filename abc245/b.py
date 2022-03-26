n = int(input())
aa = set(map(int, input().split()))

for b in range(2002):
    if b not in aa:
        print(b)
        exit()