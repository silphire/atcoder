n = int(input())
s = input()
x = s[0:n//2] 
if x + x == s:
    print("Yes")
else:
    print("No")
