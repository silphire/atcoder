k = int(input())
a, b = map(int, input().split())

while a <= b:
    if a % k == 0:
        print("OK")
        exit(0)
    a += 1
print("NG")