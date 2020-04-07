n = int(input())
aa = list(map(int, input().split()))

mina = abs(aa[0])
nm = 0
for i in range(n):
    mina = min(mina, abs(aa[i]))
    if aa[i] < 0:
        nm += 1

if nm % 2 == 1 and mina > 0:
    print(sum(map(abs, aa)) - 2 * mina)
else:
    print(sum(map(abs, aa)))