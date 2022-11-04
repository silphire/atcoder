t = int(input())
for _ in range(t):
    n2, n3, n4 = map(int, input().split())
    n6 = n3 // 2
    n10 = 0
    
    x = min(n6, n4)
    n6 -= x
    n4 -= x
    n10 += x

    x = min(n6, n2 // 2)
    n6 -= x
    n2 -= x * 2
    n10 += x

    x = min(n4 // 2, n2)
    n4 -= x * 2
    n2 -= x
    n10 += x

    x = min(n4, n2 // 3)
    n4 -= x
    n2 -= x * 3
    n10 += x

    n10 += n2 // 5
    
    print(n10)