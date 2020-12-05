n = int(input())
x = 1
arr = [a for a in range(2, n + 1)]
for i in range(len(arr)):
    x *= arr[i]
    for j in range(i + 1, len(arr)):
        if arr[j] % arr[i] == 0:
            arr[j] //= arr[i]
print(x + 1)
