a, b, c = map(int, input().split())
k = int(input())

m = max([a, b, c])
s = a + b + c - m + m * 2 ** k
print(s)