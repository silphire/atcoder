n, a, b = map(int, input().split())
cc = list(map(int, input().split()))
for i, c in enumerate(cc):
    if a + b == c:
        print(i + 1)