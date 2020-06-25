n = int(input())
pp = [0] * n
for i in range(n):
    pp[i] = int(input())

pp = sorted(pp)
pp[-1] //= 2
print(sum(pp))