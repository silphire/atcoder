n = int(input())
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))
ans = [x[2] + 1 for x in sorted([(-(aa[i] + bb[i]), -aa[i], i) for i in range(n)])]
print(' '.join(map(str, ans)))