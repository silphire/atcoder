s = list(input().rstrip())
k = int(input())
cnt = [(ord('z') - ord(c) + 1) % 26 for i, c in enumerate(s)]

for i, c in enumerate(cnt):
    if k >= c:
        k -= c
        s[i] = 'a'
if k > 0:
    s[-1] = chr((ord(s[-1]) - ord('a') + k) % 26 + ord('a'))
print(''.join(s))