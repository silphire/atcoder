a = []
for _ in range(5):
    a.append(int(input()))
k = int(input())

for i in range(5):
    for j in range(i + 1, 5):
        if abs(a[i] - a[j]) > k:
            print(":(")
            exit(0)
print("Yay!")
