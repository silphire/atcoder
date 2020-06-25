n = int(input())
s = []
for i in range(5):
    s.append(input().rstrip())

code = {
    '###.###': 0,
    '##.#..#': 1,
    '#.###.#': 2,
    '#.##.##': 3,
    '.###.#.': 4,
    '##.#.##': 5,
    '##.####': 6,
    '#.#..#.': 7,
    '#######': 8,
    '####.##': 9,
}

ans = ''
for i in range(n):
    st = i * 4
    p = ''
    p += s[0][st + 2]
    p += s[1][st + 1]
    p += s[1][st + 3]
    p += s[2][st + 2]
    p += s[3][st + 1]
    p += s[3][st + 3]
    p += s[4][st + 2]
    ans += str(code[p])
print(ans)
