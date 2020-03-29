s = input()
for c in s:
    if str.isalpha(c):
        print("error")
        exit(0)
print(int(s) * 2)