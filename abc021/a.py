n = int(input())
ans = []
x = 1
while n > 0:
    if n & 1 != 0:
        ans.append(x)
    n >>= 1
    x <<= 1
print(len(ans))
for a in ans:
    print(a)