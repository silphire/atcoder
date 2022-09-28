import datetime

s = datetime.datetime.strptime(input().rstrip(), '%Y-%m-%d').date()
t = datetime.datetime.strptime(input().rstrip(), '%Y-%m-%d').date()
ans = 0
for x in range((t - s).days + 1):
    d = s + datetime.timedelta(days=x)
    if d.weekday() >= 5:
        ans += 1
print(ans)