import bisect

n, k = map(int, input().split())
d = set(input().rstrip().split())

nums = []
for i in range(1, 100000):
    if set(list(str(i))) & d:
        continue
    nums.append(i)

p = bisect.bisect_left(nums, n)
print(nums[p])