l, h = map(int, input().split())
n = int(input())
for i in range(n):
    a = int(input())
    if a > h:
        print(-1)
    else:
        print(max(0, l - a))