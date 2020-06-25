n = int(input())
aa = tuple(map(int, input().split()))
if len(set(aa)) == n:
    print("YES")
else:
    print("NO")