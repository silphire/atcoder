a, b, c = map(int, input().split())
ans = b // c * c
if ans < a:
    print(-1)
else:
    print(ans)