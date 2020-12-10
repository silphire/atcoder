s = input().rstrip()
print(['no', 'yes'][int(len(set(s)) == len(s))])
