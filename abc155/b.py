n = int(input())
aa = list(map(int, input().split()))

for a in aa:
    if a % 2 == 0 and not (a % 3 == 0 or a % 5 == 0):
        print("DENIED")
        exit(0)
print("APPROVED")