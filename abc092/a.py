aa = [0] * 4
for i in range(4):
    aa[i] = int(input())
print(min(aa[:2]) + min(aa[2:]))
