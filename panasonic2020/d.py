n = int(input())
tb = 'abcdefghijklmnopqrstuvwxyz'

def output(s, m):
    if len(s) == n:
        print(s)
    else:
        for i in range(m + 1):
            if i == m:
                output(s + tb[i], m + 1)
            else:
                output(s + tb[i], m)
output("", 0)
