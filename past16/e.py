x = input()
if x[0] == "1" and (len(x) == 1 or set(list(x[1:])) == set("0")):
    print(len(x) - 1)
else:
    print(len(x))
