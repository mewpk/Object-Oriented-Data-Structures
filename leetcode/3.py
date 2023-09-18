class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data, root):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insert(data, root.left)
        elif data > root.data:
            root.right = self.insert(data, root.right)
        return root

    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, root, data):
        if root is None:
            print("Error! Not Found DATA")
            return root
        if data < root.data:
            root.left = self.delete(root.left, data)
        elif data > root.data:
            root.right = self.delete(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.data = self.find_min(root.right).data
            root.right = self.delete(root.right, root.data)
        return root

def printTree90(node, level = 0):
    if node != None:
        if node.data != None:
            printTree90(node.right, level + 1)
            print('     ' * level, node.data)
            printTree90(node.left, level + 1)
def parse_input(input_str):
    commands = input_str.strip().split(',')
    return commands

# Main program
tree = BinarySearchTree()
input_str = input("Enter Input : ")
commands = parse_input(input_str)

for command in commands:
    if command[0] == 'i':
        print("insert", command[2:])
        data = int(command[2:])
        tree.root = tree.insert(data, tree.root)
    elif command[0] == 'd':
        print("delete", command[2:])
        data = int(command[2:])
        tree.root = tree.delete(tree.root, data)
    printTree90(tree.root)
