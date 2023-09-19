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

