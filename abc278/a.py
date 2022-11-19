n, k = map(int, input().split())
aa = list(map(int, input().split()))
print(*(aa + [0] * k)[k:])