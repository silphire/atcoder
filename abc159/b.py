def palindrome(s):
    f = True
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            f = False
            break
    return f

s = input().rstrip()

n = len(s)
p1 = (n - 1) // 2
p2 = (n + 3) // 2
if palindrome(s) and palindrome(s[:p1]) and palindrome(s[p2-1:]):
    print("Yes")
else:
    print("No")