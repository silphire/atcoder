n = int(input())
s = [None] * n
a = [0] * n
for i in range(n):
    s[i], a[i] = input().split()
    a[i] = int(a[i])
mina = float('inf')
mini = 0
for i in range(n):
    if mina > a[i]:
        mina = a[i]
        mini = i
for i in range(n):
    print(s[(mini + i) % n])
