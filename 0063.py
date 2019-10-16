ans = 0
while True:
    try:
        s = str(input())
        if s == s[::-1]: ans += 1
    except:
        break
print (ans)
