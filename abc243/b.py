n = int(input())
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))

h = 0
b = 0
for i in range(n):
    for j in range(n):
        if aa[i] == bb[j]:
            if i == j:
                h += 1
            else:
                b += 1
print(h)
print(b)