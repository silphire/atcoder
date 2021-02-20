import sys

sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7
input = sys.stdin.readline

x = int(input())
print(100 - x % 100)