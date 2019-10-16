class Stack:
    def __init__(self):
        self.item = []
    def isEmpty(self):
        return self.item == []
    def pop(self):
        return self.item.pop()
    def push(self, items):
        return self.item.append(items)

a = Stack()

while True:
    try:
        n = int(input())
        if (n):
            a.push(n)
        else:
            print(a.pop())

    except EOFerror:
        break