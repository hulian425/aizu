import collections

def judge(card, cnt):
    nmax = cnt[0][1]
    if nmax == 4: return "four card"
    if nmax == 3: return "full house" if cnt[1][1] == 2 else "three card"
    if nmax == 2: return "two pair" if cnt[1][1] == 2 else "one pair"
    if (card[0] == 1 and list(range(10, 14)) == card[1:]) or list(range(card[0], card[0] + 5)) == card : return "straight"

    return "null"
while True:
    try:
        card = list(map(int, input().split(",")))
    except:
        break
    cnt = collections.Counter(card)
    print(judge(sorted(card), sorted(cnt.items(), key = lambda x:-x[1])))