a = []
while True:
    try:
        a = list(map(int, input()))
    except:
        break
    for i in range(9,0,-1):
        for j in range(1,i+1):a[j-1]=(a[j-1]+a[j])%10
    print(a[0])
