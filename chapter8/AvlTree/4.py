# Chapter : 8 - item : 4 - แฟ้มเอกสารสีฟ้า (Blue Archive)
#     ในเมืองแห่งหนึ่งที่มีชื่อว่า คิโวโทส (Kivotos) ซึ่งสภาองค์กรนักเรียนของเราจะมีการ
# เก็บรายชื่อนักเรียนในเมืองแบบ AVL Tree เรียกว่า "แฟ้มเอกสารสีฟ้า" โดยจะเก็บ data (ชื่อนักเรียน) 
# และ key(ค่าของชื่อ โดยให้นำค่า ASCII ของตัวอักษรแต่ล่ะตัวในชื่อมาบวกกัน เช่น 
# Arisu ก็จะเป็น 65+114+105+115+117=516 ก็จะเป็นค่า key ของนักเรียนคนนี้) ทางสภาองค์กรนักเรียน 
# ต้องการเซนเซย์อย่างคุณ ช่วยเหลือสภาองค์กรนักเรียนทำ "แฟ้มเอกสารสีฟ้า" นี้ ให้สมบูรณ์ สู้ๆนะคะ เซนเซย์ จาก Arona

# ข้อมูลนำเข้า

# I data        นำชื่อนักเรียนเข้า "แฟ้มเอกสารสีฟ้า"

# D data      นำชื่อนักเรียนออก "แฟ้มเอกสารสีฟ้า"

# P               แสดงข้อมูลของ "แฟ้มเอกสารสีฟ้า"



# ข้อมูลนำออกของ P

#      การแสดงข้อมูลจะเป็นแบบ Tree Directory เผื่อไม่เห็นภาพ

# 'Root (Root.key)'

#     'Left (Left.key)'

#         'Left->Left (Left->Left.key)"

#         *

#     'Right (Right.key)'

#         'Right->Left (Right->Left.key)

#         'Right->Right (Right->Right.key)

# ถ้าใน "แฟ้มเอกสารสีฟ้า" ไม่มี Left หรือ Right (ต้องมีอย่างใดอย่างนึง)
#  ให้แสดง * แทนในส่วนที่ไม่มี (ตามตัวอย่าง) แต่ถ้าไม่มีทั้ง Left และ Right ก็ไม่ต้องแสดงอะไรเลย 
# เพราะ เป็น leaf ของ AVL Tree

# ทางองค์กรนักเรียนได้ทำการวาง Prototype ไว้แล้วตามนี้

# def nameValue(val):
#     # Code Here


# class TreeNode(object):
#     def __init__(self, val):
#         # Code Here


# class AVL_Tree(object):
#     def insert(self, root, data):
#         # Code Here

#     def delete(self, root, data):
#         # Code Here

#     def leftRotate(self, z):
#         # Code here

#     def rightRotate(self, z):
#         # Code here

#     def getHeight(self, root):
#         # Code here

#     def getBalance(self, root):
#         # Code here

#     def getMinValueNode(self, root):
#         # Code here

#     def printTree(self, root, level=0):
#         # Code here


# avl_tree = AVL_Tree()
# root = None
# inp = input("Enter the data of your friend: ").split(",")
# print("------------------------------")
# for i in inp:
#     op, *data = i.split(" ")
#     data = data[0] if data else ""
#     if op == "I":
#         root = avl_tree.insert(root, data)
#     elif op == "D":
#         root = avl_tree.delete(root, data)
#     elif op == "P":
#         avl_tree.printTree(root)
#         print("------------------------------")

# Calculate the sum of ASCII values of characters in a string
def nameValue(st):
    return sum([ord(i) for i in st])

# Define a Node class for the AVL Tree
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return self.data + f" ({nameValue(self.data)})"

# Define the AVL_Tree class
class AVL_Tree(object):
    def insert(self, root, data):
        if not root:
            return Node(data)
        if nameValue(data) < nameValue(root.data):
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        
        # Check balance and perform rotations if necessary
        
        return self._balance(root)
    
    def _balance(self, root):

        balance = self.getBalance(root)

        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rotateRight(root)
 
        # Case 2 - Right Right
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.rotateLeft(root)
 
        # Case 3 - Left Right
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)
 
        # Case 4 - Right Left
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)
 
        return root
    
    
    def delete(self, root, data):
        if not root:
            return root
        if nameValue(data) < nameValue(root.data):
            root.left = self.delete(root.left, data)
        elif nameValue(data) > nameValue(root.data):
            root.right = self.delete(root.right, data)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)
        
        if root is None:
            return root
        
        # Check balance and perform rotations if necessary
 
        return self._balance(root)

    def rotateRight(self, root):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root
        return new_root
    
    def rotateLeft(self, root):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        return new_root
    
    def height(self, root):
        if not root:
            return 0 
        return 1 + max(self.height(root.left), self.height(root.right))

    def getBalance(self, root):
        return self.height(root.left) - self.height(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)
    
    # Print the AVL tree in a structured format
    def printTree(self, node, level=0):
        if node != None:
            print('    ' * level , node, sep="")
            if node.left or node.right:
                if node.left:
                    self.printTree(node.left, level + 1)
                else: 
                    print('    ' * (level+1), "*", sep="")
                if node.right:
                    self.printTree(node.right, level + 1)
                else:
                    print('    ' * (level+1), "*", sep="")
                  
# Create an instance of the AVL_Tree class
avl_tree = AVL_Tree()
root = None

# Input data from the user
inp = input("Enter the data of your friend: ").split(",")
print("------------------------------")

# Process input commands (I for insert, D for delete, P for print)
for i in inp:
    op, *data = i.split()
    data = data[0] if data else ""
    if op == "I":
        root = avl_tree.insert(root, data)
    elif op == "D":
        root = avl_tree.delete(root, data)
    elif op == "P":
        avl_tree.printTree(root)
        print("------------------------------")
