n = int(input())
s = input()

st = set()
for i, c in enumerate(s):
    st.add(c)
    if len(st) == 3:
        print(i + 1)
        exit()