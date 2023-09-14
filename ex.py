# Chapter : 7 - item : 1 - รู้จักกับ Binary Search Tree
# ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input 
# ตัวแรกสุดจะเป็น Root เสมอ

dict = {}


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
    def insert(self, data , root ):
        if root is None :
            n = Node(data)
            return n

    def getlevel(self, node, level = 0):
        if node != None:
            if node.data not in dict:
                dict[level] = [node.data]
            else :
                dict[level] += [node.data]
            self.getlevel(node.left, level + 1)
            self.getlevel(node.right, level + 1)
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
root = None
T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i , root)
T.getlevel(root)
print(dict)
# T.printTree(root)