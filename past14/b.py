d = int(input())
a = list(map(int, input().split('.')))
b = list(map(int, input().split('.')))
c = [
    a[0] + b[0],
    a[1] + b[1],
]
c[0] += c[1] // (10 ** d)
c[1]  = c[1] %  (10 ** d)
print(f'{c[0]}.{c[1]:0{d}d}')