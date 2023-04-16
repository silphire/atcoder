from collections import deque

MOD = 998244353
q = int(input())
que = deque([1])
s = 1
for _ in range(q):
    c, *a = map(int, input().split())
    if c == 1:
        s = s * 10 + a[0]
        s %= MOD
        que.append(a[0])
    elif c == 2:
        x = que.popleft()
        x *= pow(10, len(que), MOD)
        x %= MOD
        s -= x
        s += MOD
        s %= MOD
    else:
        print(s % MOD)