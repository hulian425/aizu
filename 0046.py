m={'A':0,'B':1,'C':2}
a = 'A'
b='B'
while True:
    try:
        a, b = list(input().split(','))
    except:
        break
    m[a],m[b]=m[b],m[a]

if m['A']==0:  print('A')
elif m['B']==0:   print ('B')
elif m['C']==0:  print('C')




