s = input().rstrip()
for i in range(len(s) - 1):
  if s[i] == s[i + 1]:
    print("Bad")
    exit(0)
print("Good")