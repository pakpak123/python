class Stack:
    def __init__(self):
        self.items = []

    def push(self, i):
        self.items.append(i)

    def pop(self):
        if not self.isEmpty():
            self.items.pop()
        return -1

    def top(self):
        if not self.isEmpty():
            return self.items[-1]
        return -1

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)


print("******** Parking Lot ********")
m, s, o, n = input("Enter max of car,car in soi,operation : ").split()
m, n = int(m), int(n)
A1 = Stack()
A2 = Stack()
car = s.split(',')
for i in car:
    if (int(i) != 0):
        A1.push(int(i))
if o == 'arrive':
    if A1.size() == m:
        print("car", n, "cannot arrive : Soi Full")
    elif n in A1.items:
        print("car", n, "already in soi")
    else:
        A1.push(n)
        print("car", n, "arrive! : Add Car", n)
elif o == 'depart':
    if int(s[0]) == 0:
        print("car", n, "cannot depart : Soi Empty")
    elif n not in A1.items:
        print("car", n, "cannot depart : Dont Have Car", n)
    else:
        while (A1.top() != n):
            A2.push(A1.top())
            A1.pop()
        A1.pop()
        while (A2.size() != 0):
            A1.push(A2.top())
            A2.pop()
        print("car", n, "depart ! : Car", n, "was remove")
print([e for e in A1.items])