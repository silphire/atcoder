abc = input().rstrip()
ans = int(abc) + int(abc[1:] + abc[0]) + int(abc[-1] + abc[:-1])
print(ans)