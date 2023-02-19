n, k = map(int, input().split())
aa = list(map(int, input().split()))

x = sorted(set(aa))[:k]
k = min(k, len(x))
for i in range(k):
    if x[i] != i:
        print(i)
        exit()
print(k)