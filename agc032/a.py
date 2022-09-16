n = int(input())
bb = tuple(map(int, input().split()))

def dfs(arr, ops):
    if not arr:
        for x in reversed(ops):
            print(x)
        exit()

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == i + 1:
            dfs(arr[:i] + arr[i+1:], ops + (i + 1,))
            break

dfs(bb, ())
print(-1)