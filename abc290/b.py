n, k = map(int, input().split())
s = input()

t = ''
for c in s:
    if c == 'o' and k > 0:
        t += 'o'
        k -= 1
    else:
        t += 'x'
print(t)