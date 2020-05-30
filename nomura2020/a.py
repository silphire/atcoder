h1, m1, h2, m2, k = map(int, input().split())
m = (h2 - h1) * 60 + (m2 - m1)
print(m - k)