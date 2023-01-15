s = input()
n = len(s)

x = 0
for i in range(n):
    a = ord(s[-i - 1]) - ord('A') + 1
    x += a * 26 ** i
print(x)