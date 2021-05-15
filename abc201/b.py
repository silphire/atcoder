n = int(input())
a = [None] * n
for i in range(n):
    s, t = input().rstrip().split()
    a[i] = (int(t), s)
print(sorted(a)[-2][1])