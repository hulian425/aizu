while True:
    try:
        n = int(input())
        num = 0
        for a in range(10):
            for b in range(10):
                for c in range(10):
                    for d in range(10):
                        if (a + b + c + d == n):
                            num += 1
        print(num)
    except EOFError:
        break
