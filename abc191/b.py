import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

n, x = map(int, input().split())
aa = [a for a in map(int, input().split()) if a != x]

print(' '.join(map(str, aa)))