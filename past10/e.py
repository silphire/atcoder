import datetime

s = map(int, input().split('/'))
d = datetime.date(*s)
ds = d.strftime('%Y/%m/%d')
while len(set(tuple(ds))) > 3:
    d = d + datetime.timedelta(days=1)
    ds = d.strftime('%Y/%m/%d')
print(ds)
