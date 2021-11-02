class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
            return self.root
        p = self.root
        filled = False
        while not filled:
            if p.data > data:
                if p.left == None:
                    p.left = Node(data)
                    filled = True
                else:
                    p = p.left
            else:
                if p.right == None:
                    p.right = Node(data)
                    filled = True
                else:
                    p = p.right
        return self.root

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

seventeen = []
def inorderUntil(node, n):
    global seventeen
    if node != None:
        inorderUntil(node.left, n)
        if node.data >= n:
            return
        seventeen.append(str(node.data))
        inorderUntil(node.right, n)

T = BST()
inp1, inp2 = input('Enter Input : ').split('|')
inp1 = [int(i) for i in inp1.split()]
inp2 = int(inp2)
for i in inp1:
    root = T.insert(i)
T.printTree(root)

inorderUntil(root, inp2)

print('--------------------------------------------------')
print(f'Below {inp2} : { "Not have" if seventeen == [] else " ".join(seventeen) }')
