from collections import Counter
n = int(input())
t = input().rstrip()

if t in '110' * ((n // 3 + 1) * 2):
    if t == '1':
        print(2 * 10 ** 10)
    elif t == '11':
        print(10 ** 10)
    else:
        ctr = Counter(t)
        if t[-1] == '0':
            print(10 ** 10 - ctr['0'] + 1)
        else:
            print(10 ** 10 - ctr['0'])

else:
    print(0)