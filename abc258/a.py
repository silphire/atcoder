k = int(input())
m = 21
if k >= 60:
    m += 1
    k -= 60
print(f'{m:02d}:{k:02d}')