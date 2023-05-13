from collections import Counter

s = input()
t = input()

cs = Counter(list(s))
ct = Counter(list(t))

for ch in cs:
    if ch == '@':
        continue
    n = min(cs[ch], ct[ch])
    cs[ch] -= n
    ct[ch] -= n

for ch in ct:
    if ch == '@':
        continue
    n = min(cs[ch], ct[ch])
    ct[ch] -= n
    ct[ch] -= n

avs = cs['@']
avt = ct['@']
for ch in 'atcoder':
    avt -= cs[ch]
    cs[ch] = 0
    avs -= ct[ch]
    ct[ch] = 0

if avs >= 0 and avt >= 0 and sum(cs.values()) == cs['@'] and sum(ct.values()) == ct['@']:
    print('Yes')
else:
    print('No')