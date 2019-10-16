def f(n):
    if n <= 48.0:
        print("light fly")
    elif 48< n <=51:
        print("fly")
    elif 51 < n <= 54:
        print("bantam")
    elif 54 < n <= 57:
        print("feather")
    elif 57 < n <=60:
        print("light")
    elif 60 < n <=64:
        print("light welter")
    elif 64 < n <=69:
        print("welter")
    elif 69 < n <=75:
        print("light middle")
    elif 75 < n <=81:
        print("middle")
    elif 81 < n <= 91:
        print("light heavy")
    elif n>91:
        print("heavy")


while True:
    try:
        n = float(input())
    except:
        break
    f(n)
