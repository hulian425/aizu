while True:
    try:
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
    except:
        break
    hit = blow = 0
    for i in range(4):
        if (a[i] == b[i]):
            hit += 1
            b[i] = -1
    for i in range(4):
        if b[i] >= 0:
            if b[i] in a:
                 blow += 1
    print(hit, blow)

