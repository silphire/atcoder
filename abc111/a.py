n = input().rstrip()
d = {'1': '9', '9': '1'}
m = ''
for i in range(len(n)):
    m += d.get(n[i], n[i])
print(m)
