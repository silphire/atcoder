x, a, b, c = map(int, input().split())
r = x / a + c
t = x / b
if r < t:
    print("Hare")
elif r > t:
    print("Tortoise")
else:
    print("Tie")