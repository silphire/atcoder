import statistics

n = int(input())
aa = [None] * n
bb = [None] * n
for i in range(n):
    a, b = map(int, input().split())
    aa[i] = a
    bb[i] = b

def median(arr):
    if len(arr) % 2 == 0:
        return (arr[n // 2 - 1] + arr[n // 2]) / 2
    else:
        return arr[n // 2]

m = n
if n % 2 == 0:
    m *= 2
medmin = median(sorted(map(lambda x: x * m, aa)))
medmax = median(sorted(map(lambda x: x * m, bb)))

print(int((medmax - medmin) / n) + 1)