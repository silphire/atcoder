import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

v, t, s, d = map(int, input().split())
if t <= d / v <= s:
    print('No')
else:
    print('Yes')