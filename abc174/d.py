n = int(input())
cc = input().rstrip()

sc = ''.join(sorted(cc))
x = 0
for i in range(n):
    if cc[i] != sc[i]:
        x += 1
print((x + 1) // 2)