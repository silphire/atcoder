def is_choku(s):
    if not s:
        return True
    elif s.endswith('ch'):
        return is_choku(s[:-2])
    elif 'oku'.find(s[-1]) >= 0:
        return is_choku(s[:-1])
    else:
        return False
if is_choku(input().rstrip()):
    print('YES')
else:
    print('NO')