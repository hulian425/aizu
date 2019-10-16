m = {'A':0, 'B':0, 'AB':0, 'O':0}
while True:
    try:
        a,b = list(input().split(','))
    except:
        break
    if b == 'A':    m['A']+=1
    if b == 'B':    m['B']+=1
    if b == 'AB':   m['AB']+=1
    if b == 'O':    m['O']+=1
print(m['A'],m['B'],m['AB'],m['O'], sep = '\n')