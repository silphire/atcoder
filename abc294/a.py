n = int(input())
aa = list(map(int, input().split()))
bb = [a for a in aa if a % 2 == 0]
print(*bb)