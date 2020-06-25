s = input().rstrip()
t = input().rstrip()
if s == t:
    print("same")
elif s.lower() == t.lower():
    print("case-insensitive")
else:
    print("different")