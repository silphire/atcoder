n = int(input()) - 1
ans = ''
for i in range(10):
    if (n >> i) & 1 == 0:
        ans = '4' + ans
    else:
        ans = '7' + ans
print(ans)