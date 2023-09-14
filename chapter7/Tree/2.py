# Chapter : 7 - item : 2 - หาค่า Min และ Max

# ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input
# ตัวแรกสุดจะเป็น Root เสมอ และหาค่าที่น้อยและมากที่สุดของ Binary Search Tree

# ***** ห้ามใช้ Built-in Function เช่น min() , max() , sort() , sorted()


class Node :
    def __init__(self,data) -> None:
        self.data = data
        self.left = self.right = None
    def __str__(self) -> str:
        return str(self.data)

class BST :
    def __init__(self) -> None:
        self.root = None
        self.min = None
        self.max = None
    def insert(self, data , root ):
        # Code Here
        if root is None:
            n = Node(data)
            # print('insert :',self.root)
            if self.min is None and self.max is None:
                self.min = data
                self.max = data
            if data > self.max :
                self.max = data
            elif data < self.min:    
                self.min = data
            return n
        else:
            if data < root.data:
                root.left = self.insert( data,root.left)
            else:
                root.right = self.insert( data ,root.right)
        return root
    
    # Optional function

    # def find_min_max(self, node ,level = 0 ):
    #     if node != None:
    #         if node.data < self.min:
    #             self.min = node.data
    #         if node.data > self.max:
    #             self.max = node.data
    #         self.find_min_max(node.right, level + 1)
    #         self.find_min_max(node.left, level + 1)

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
T.printTree(root)
print("-"*50)
print(f"Min : {T.min}")
print(f"Max : {T.max}")