n = int(input())
ss = set()
for i in range(n):
    s = input().rstrip()
    ss.add(s)
for s in ss:
    if ('!' + s) in ss or ('!!' + s) in ss:
        print(s)
        exit()
print('satisfiable')