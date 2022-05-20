input()
ans = []
for x in range(1, 100):
    ans.append(x)
    ans.append(x * 100)
    ans.append(x * 10000)
print(len(ans))
print(*sorted(ans))