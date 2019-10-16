while True:
    try:
        a = []
        a.append(float(input()))
    except:
        break
    for i in range(2,11):
        a.append(a[i - 2]*2 if i%2==0 else a[i-2]/3)
    print(sum(a))