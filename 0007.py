n = int(input())
w = 100000
for i in range(n):
    w *= 1.05
    if (w % 1000):
        w = w // 1000 + 1
    else:
        w = w // 1000
    w *= 1000
print(int(w))