s = [list(map(lambda x: {'a':0, 'b':1, 'c':2}[x], input().rstrip())) for _ in range(3)]
i = [0] * 3
t = 0
while True:
    if i[t] == len(s[t]):
        print('ABC'[t])
        exit()
    c = s[t][i[t]]
    i[t] += 1
    t = c