a, b = map(int, input().split())
a -= 1
b -= 1
if (a + 1) % 10 == b or a == 0 and b == 9:
    print('Yes')
else:
    print('No')