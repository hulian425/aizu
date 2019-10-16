n=int(input())
while(n):
    n-=1
    a = list(input())
    print(int("".join(sorted(a, reverse=True))) - int("".join(sorted(a))))