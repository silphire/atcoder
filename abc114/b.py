s = input().rstrip()
x = 10000
for i in range(len(s) - 3 + 1):
    x = min(x, abs(753 - int(s[i:i+3])))
print(x)
