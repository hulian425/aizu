w = int(input())
n = int(input())
a = range(w)
a = list(a)
for i in range(n):
    p, q = map(int, input().split(","))
    swap(a[p-1], a[q-1])
for each in a:
    print(each + 1)
