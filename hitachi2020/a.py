s = input().rstrip()

for i in range(1, 6):
    if s == "hi" * i:
        print("Yes")
        exit()
print("No")