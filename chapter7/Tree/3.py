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
        self.count = 0
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
    

    def less_than_or_equal(self, node , number ,level = 0 ):
        if node != None:
            if node.data <= number:
                self.count += 1
            self.less_than_or_equal(node.right,number, level + 1)
            self.less_than_or_equal(node.left,number, level + 1)

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

root = None
T = BST()
inp = [int(part) if '/' not in part else int(sub_part) for part in input("Enter Input : ").split() for sub_part in part.split('/')]
for i in inp[:-1]:
    root = T.insert(i , root)
T.printTree(root)
print("-"*50)
T.less_than_or_equal(root,inp[-1])
print(T.count)