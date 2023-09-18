# Chapter : 7 - item : 4 - delete node in tree

# ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ

# โดยมีการป้อน input ดังนี้

# i <int> = insert data

# d <int> = delete data

# หมายเหตุ การลบนั้นจะใช้หลักการของ Inorder Successor และ จำนวน parameter มีได้มากสุด 3 ตัว

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


# class Node:
#     def __init__(self, data): 
#         self.data = data  
#         self.left = None  
#         self.right = None 
#         self.level = None 

#     # def __str__(self):
#     #     return str(self.data) 

# class BinarySearchTree:
#     def __init__(self) -> None:
#         self.root = None
#         self.min = None
#     def insert(self, data , root ):
#         # Code Here
#         if root is None or root.data == None:
#             n = Node(data)
#             # print('insert :',self.root)
#             return n
#         else:
#             if data < root.data:
#                 root.left = self.insert( data,root.left)
#             else:
#                 root.right = self.insert( data ,root.right)

#         return root
        
#     def least_number(self, node, number):
#         if node is not None:
#             if node.data <= number:
#                 number = node.data

#             # Recursively search in the right and left subtrees, and update the number.
#             number = self.least_number(node.right, number)
#             number = self.least_number(node.left, number)

#         # Store the minimum value in the instance variable.
#         self.min = number

#         return number

    
#     def find_node(self, node, data):
#         if node is None:
#             return None  # If the current node is None, return None to indicate the data was not found.

#         if node.data == data:
#             return node  # If the current node's data matches the target data, return the current node.

#         # Recursively search in the right and left subtrees.
#         result_right = self.find_node(node.right, data)
#         if result_right is not None:
#             return result_right  # If found in the right subtree, return the result.

#         result_left = self.find_node(node.left, data)
#         if result_left is not None:
#             return result_left  # If found in the left subtree, return the result.

#         return None  # If not found in both subtrees, return None.
#     def find_node_V2(self, node, data):
#         if node is None:
#             return None  # If the current node is None, return None to indicate the data was not found.

#         if node.right.data == data or node.left.data == data:
#             return node  # If the current node's data matches the target data, return the current node.

#         # Recursively search in the right and left subtrees.
#         result_right = self.find_node(node.right, data)
#         if result_right is not None:
#             return result_right  # If found in the right subtree, return the result.

#         result_left = self.find_node(node.left, data)
#         if result_left is not None:
#             return result_left  # If found in the left subtree, return the result.

#         return None  # If not found in both subtrees, return None.

#     def delete(self,r, data):
#         #code here
#         self.min = None
#         node = self.find_node(r,data)
#         if node == None:
#             print('Error! Not Found DATA')
#             return
#         if node.right == None or node.right.data == None:
#             if node.left != None and node.left.data != None:
#                 # print(node.data,node.left.data)
#                 if node is r:
#                     self.root = node.left
#                     return
#                 prev_node = self.find_node_V2(r,data)
#                 prev_node.right = node.left
#             else :
#                 node.data = None
#         else :
#             self.least_number(node.right,node.right.data)
#             # print('min :',self.min)
#             node_swap = self.find_node(node.right,self.min)
#             node.data = self.min
#             node_swap.data = None
#             node_swap = None
                
# def printTree90(node, level = 0):
#     if node != None:
#         if node.data != None:
#             printTree90(node.right, level + 1)
#             print('     ' * level, node.data)
#             printTree90(node.left, level + 1)


# tree = BinarySearchTree()
# data = input("Enter Input : ").split(",")
# #code here
# for i in data:
#     if i[0] == 'i':
#         print('insert',i[2:])
#         tree.root = tree.insert(int(i[2:]),tree.root)
#     elif i[0] == 'd':
#         print('delete',i[2:])
#         tree.delete(tree.root,int(i[2:]))
#     printTree90(tree.root)