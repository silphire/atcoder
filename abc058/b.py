o = input().rstrip()
e = input().rstrip()
x = ''
for i in range(len(o)):
    x += o[i]
    if i < len(e):
        x += e[i]
print(x)
