n = int(input())
aa = list(map(int, input().split()))

mini = -1
mina = float('inf')
avg = sum(aa) / n
for i, a in enumerate(aa):
    if abs(avg - mina) > abs(avg - a):
        mina = a
        mini = i
print(mini)