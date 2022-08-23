q, h, s, d = map(int, input().split())
n = int(input()) * 4

h = min(h, q * 2)
s = min(s, h * 2)
d = min(d, s * 2)
print((n >> 3) * d + ((n >> 2) & 1) * s + ((n >> 1) & 1) * h + (n & 1) * q)