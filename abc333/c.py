n = int(input())

u = [1]
for i in range(1, 111):
    u.append(u[-1] * 10 + 1)

aa = set()
for i in range(12):
    for j in range(12):
        for k in range(12):
            aa.add(u[i] + u[j] + u[k])
aa = sorted(aa)
print(aa[n - 1])