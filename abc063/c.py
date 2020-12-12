n = int(input())
s = [None] * n
for i in range(n):
    s[i] = int(input())

s = list(sorted(s))
ans = sum(s)
if ans % 10 != 0:
    print(ans)
    exit()

for i in range(n):
    if s[i] % 10 == 0:
        continue
    x = ans - s[i]
    if x % 10 != 0:
        print(x)
        exit()
print(0)