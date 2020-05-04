import re

s = input().rstrip()

ss = 'abcdefghijklmnopqrstuvwxyz.'
m = set()
for i in range(len(ss)):
    for j in range(len(ss)):
        for k in range(len(ss)):
            t = ss[i] + ss[j] + ss[k]
            for n in range(1, 4):
                if re.search(t[:n], s):
                    m.add(t[:n])
print(len(m))
