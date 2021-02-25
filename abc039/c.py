s = input().rstrip()
k = "WBWBWWBWBWBW" * 10
scale = ["Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "So", "So#", "La", "La#", "Si"]
n = k.find(s)
print(scale[n % len(scale)])