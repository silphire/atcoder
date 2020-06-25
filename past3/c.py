a, r, n = map(int, input().split())
 
x = a
if r == 1:
    print(x)
    exit(0)
for i in range(n - 1):
    if x > 10 ** 9:
        print("large")
        exit(0)
    x *= r

if x > 10 ** 9:
    print("large")
else:
    print(x)