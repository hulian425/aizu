roman = {"I":1, 'V':5, 'X':10, 'L':50,'C':100, "D":500,'M':1000}
while True:
    try:
        p = list(input())
    except EOFError:
        break
    ans = i = 0
    while i <len(p):
        if i+1 < len(p) and roman[p[i]] < roman[p[i+1]]:
            ans = ans + roman[p[i+1]] - roman[p[i]]
            i += 1
        else:
            ans += roman[p[i]]
        i += 1
    print(ans)

