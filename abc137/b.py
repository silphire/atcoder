k, x = map(int, input().split())
mx = max(-1000000, x - k + 1)
nums = []
for i in range(k * 2 - 1):
    if mx + i > 1000000:
        break
    nums.append(mx + i)
print(*nums)
