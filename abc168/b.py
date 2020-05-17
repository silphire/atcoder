k = int(input())
s = input().rstrip()

if len(s) <= k:
    print(s)
else:
    print(s[:k] + "...")
