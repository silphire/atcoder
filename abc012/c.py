n = int(input())
t = 0
for i in range(1, 10):
    for j in range(1, 10):
        t += i * j
t -= n
ans = []
for i in range(1, 10):
    for j in range(1, 10):
        if i * j == t:
            ans.append(f'{i} x {j}')

for s in sorted(ans):
    print(s)