while True:
    try:
        d = int(input())
        sum = 0
        n = d
        while n < 600:
            sum += d * (n ** 2)
            n += d
        print(sum)
    except EOFError:
        break