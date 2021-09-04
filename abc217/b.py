a = {'ABC' , 'ARC' , 'AGC' , 'AHC'}
b = set()
for _ in range(3):
    b.add(input().rstrip())
print(list(a - b)[0])