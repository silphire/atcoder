t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    seq = []
    aa = a
    bb = b
    while True:
        while aa > bb:
            bb += b
        if seq and seq[0] == bb - aa:
            break
        seq.append(bb - aa)
        aa += a
    ls = len(seq)
    ans = sum(seq) * (n // ls) + sum(seq[:(n % ls)])
    print(ans)