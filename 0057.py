a = [1]
for i in range(1, 10002):
    a.append(a[i-1]+i)
while True:
    try:
        print(a[int(input())])
    except:
        break
