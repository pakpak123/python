class Stack:
    def __init__(self):
        self.items = []

    def push(self, i):
        return self.items.append(i)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return (len(self.items) == 0)

    def size(self):
        return len(self.items)

    def top(self):
        if self.size() != 0:
            return self.items[-1]

print(" ***Postfix expression calcuation***")
num = input('Enter Postfix expression : ').split()
s = Stack()
for i in num:
    if i not in '+-*/':
        s.push(int(i))
    if i == '+':
        y = s.pop()
        x = s.pop()
        s.push(x + y)
    elif i == '-':
        y = s.pop()
        x = s.pop()
        s.push(x - y)
    elif i == '*':
        y = s.pop()
        x = s.pop()
        s.push(x * y)
    elif i == '/':
        y = s.pop()
        x = s.pop()
        s.push(x / y)

x = s.items[0]
print("Answer :  {:0.2f}".format(x))