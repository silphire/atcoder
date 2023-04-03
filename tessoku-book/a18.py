n, s = map(int, input().split())
aa = list(map(int, input().split()))

st = set()
for a in aa:
    ns = {a + x for x in st}
    st = st | ns | {a}
if s in st:
    print('Yes')
else:
    print('No')