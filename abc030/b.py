n, m = map(int, input().split())
hr = ((n % 12) * 60 + m) / (12 * 60) * 360
mr = m * 6
print(min(abs(hr - mr), 360 - abs(hr - mr)))