k, g, m = map(int, input().split())

ag = 0
am = 0

for i in range(k):
    if ag == g:
        ag = 0
    elif am == 0:
        am = m
    else:
        d = min(am, g - ag)
        am -= d
        ag += d
print(*[ag, am])