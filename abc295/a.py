n = int(input())
ww = set(input().split())
if ww & set(['and', 'not', 'that', 'the', 'you']):
    print('Yes')
else:
    print('No')