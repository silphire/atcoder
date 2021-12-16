n = int(input())
sc = [list(map(int, input().split())) for _ in range(n)]

def check(x):
    st = set()
    for s in sc:
        b = 0
        for i in range(5):
            b = (b << 1) | int(s[i] >= x)
        st.add(b)
    for a in st:
        for b in st:
            for c in st:
                if a | b | c == 31:
                    return True
    return False


ok = 0
ng = 10 ** 9 + 1
while ng - ok > 1:
    mid = (ok + ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid
print(ok)
