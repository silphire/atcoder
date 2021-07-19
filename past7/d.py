import re

n = int(input())
s = input().rstrip()

print(re.sub(r'([aeiou])x\1', '...', s))