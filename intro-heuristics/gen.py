import random

print(365)
print(' '.join([str(random.randint(0, 100)) for _ in range(26)]))
for d in range(365):
    print(' '.join([str(random.randint(0, 20000)) for _ in range(26)]))
