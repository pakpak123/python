class Stack:
    def __init__(self):
        self.item = []

    def add(self, item):
        self.item.append(item)

    def size(self):
        return len(self.item)

    def pop(self):
        if len(self.item) == 0:
            return -1
        else:
            return self.item.pop()

    def index(self):
        return len(self.item)


Inp = input('Enter Input : ').split(',')
s = Stack()

for i in Inp:
    i = i.split()
    if i[0] == 'P':
        b = s.pop()
        c = s.index()
        if b == -1:
            print('-1')
        else:
            print('Pop =', b,'and Index =',c)
    elif i[0] == 'A':
        s.add(int(i[1]))
        a = s.size()
        print('Add =', int(i[1]),'and Size =',a)

if len(s.item) >0:
    for i in range(0,len(s.item)):
        if len(s.item) == 1:
            print("Value in Stack =",s.item[i])
        elif len(s.item) == 2:
            print("Value in Stack =",s.item[i],s.item[i+1])
        elif len(s.item) == 3:
            print("Value in Stack =",s.item[i],s.item[i+1],s.item[i+2])
else:
    print('Value in Stack = Empty')

