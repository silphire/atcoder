import heapq
n = int(input())
aa = list(map(int, input().split()))
x = 0
for i in range(n):
    while aa[i] % 2 == 0:
        aa[i] //= 2
        x += 1
heapq.heapify(aa)
for _ in range(x):
    heapq.heapreplace(aa, aa[0] * 3)
print(aa[0])