n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

for i in range(1, n):
    if a[i - 1] == a[i]:
        print("stay")
    elif a[i - 1] > a[i]:
        print("down {}".format(a[i - 1] - a[i]))
    else:
        print("up {}".format(a[i] - a[i - 1]))