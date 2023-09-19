# Chapter : 7 - item : 1 - รู้จักกับ Binary Search Tree
# ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input 
# ตัวแรกสุดจะเป็น Root เสมอ



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
        self.closest_value = None 

    def insert(self, data , root ):
        # Code Here
        if root is None:
            n = Node(data)
            # print('insert :',self.root)
            return n
        else:
            if data < root.data:
                root.left = self.insert( data,root.left)
            else:
                root.right = self.insert( data ,root.right)

        return root
    def findTree(self,node , value):
        if node != None :
            if node.data == value :
                return True
            elif node.data > value :
                return self.findTree(node.left,value)
            else :
                return self.findTree(node.right,value)
        else :
            return False
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
            
    def closestValue(self,node ,value):
        if node != None :
            self.closest_value = node.data
            if node.data == value :
                self.closest_value = node.data
                return
            elif node.data < value :
                self.closestValue(node.right,value)
            else :
                self.closestValue(node.left,value)
root = None
T = BST()
inp = [i for i in input('Enter Input : ').split()]
for i in inp[:-1]:
    root = T.insert(int(i) , root)
    T.printTree(root)
    print("--------------------------------------------------")
root = T.insert(int(inp[-1].split("/")[0]) , root)
T.printTree(root)
print("--------------------------------------------------")
k = int(inp[-1].split('/')[1])
T.closestValue(root,k)
if T.closest_value < 0 :
    if T.findTree(root,abs(T.closest_value)) :
        print(f"Closest value of {k} : {abs(T.closest_value)}")
    else :
        print(f"Closest value of {k} : {T.closest_value}")
else :
    if T.closest_value < k  and T.findTree(root,k+k-T.closest_value):
        print(f"Closest value of {k} : {k+k-T.closest_value}")
    else :
        print(f"Closest value of {k} : {T.closest_value}")