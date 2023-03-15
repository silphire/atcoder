n, x = map(int, input().split())
print(["No", "Yes"][int(x in set(map(int, input().split())))])