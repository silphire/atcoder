s = input().rstrip()
ans = 0
for i in range(len(s)):
    n = 0
    for j in range(i, len(s)):
        if s[j] not in 'ACGT':
            break
        n += 1
    ans = max(ans, n)
print(ans)
