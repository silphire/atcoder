s = [
    input().rstrip()
    for _ in range(3)
]
ans = ''
for t in list(input().rstrip()):
    ans += s[int(t) - 1]
print(ans)