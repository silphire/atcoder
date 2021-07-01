n = int(input())
s = input().rstrip()
k = int(input())

print(''.join(map(lambda x: x if x == s[k - 1] else "*", list(s))))
