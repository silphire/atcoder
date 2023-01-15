n = int(input())
s = input()

for i in range(1, n):
    x = n - i
    for j in range(n):
        if j + i >= n:
            break
        if s[j] == s[j + i]:
            x = j
            break
    print(x)