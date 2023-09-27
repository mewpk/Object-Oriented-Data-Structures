# Chapter : 8 - item : 3 - ต้นไม้หยาบ
# ต้นไม้หยาบเป็นต้นไม้แบบ Complete Binary Tree มีทั้งสิ้น N โหนด การเรียกชื่อโหนด
# จะเรียกเป็นโหนดที่ 1,2,3,... ไปเรื่อยๆจนถึงโหนดที่ N เริ่มต้นจะเติมค่าตั้งแต่โหนดที่ [N / 2] + 1 
# ไปจนถึงโหนดที่ N ต่อมาจะมีการขีดฆ่าต้นไม้หยาบ จากโหนดลูกสองโหนดใดๆที่อยู่ติดกัน 
# โดยใช้หลักการว่าโหนดพ่อจะเอาค่าของโหนดลูกที่มีค่าน้อยที่สุดขึ้นมา แล้วลบค่าของโหนดลูกทั้งสองด้วยค่านั้น 
# ให้นักศึกษาเขียนโปรแกรมเพื่อหาผลรวมโหนดภายหลังการขีดฆ่าต้นไม้หยาบ

# โดย input จะแบ่เป็น 2 ฝั่งด้วย /
# 1. ด้านซ้ายจะเป็นจำนวนโหนด (N) โดยรับประกันว่ามีจำนวนโหนดอย่างต่ำที่สุดคือ 3
# 2. value จำนวน [N / 2] + 1 ค่า เป็นค่าตั้งแต่โหนดที่ [N / 2] + 1 จนถึง N 
# และถ้าหากจำนวน value ไม่เท่ากับ [N / 2] + 1 จะแสดงผลลัพธ์เป็น "Incorrect Input"

# หมายเหตุ ต้นไม้ในข้อนี้ไม่จำเป็นต้องเป็น Perfect Binary Tree แต่จำเป็นต้องมีจำนวนโหนดเป็นเลขคี่

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
    
    def __str__(self):
        return str(self.data)

class PerfectTree():
    def insert(self, root, data):
        if not root:
            return Node(data)
        q = []
        q.append(root)
        while 1:
            cur = q.pop(0)
            if not cur.left:
                cur.left = Node(data)
                break
            elif not cur.right:
                cur.right = Node(data)
                break
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return root

def checkTree(root):
    if root:
        root.left = checkTree(root.left)
        root.right = checkTree(root.right)
        if root.right and root.left and root.right.data != '*' and root.left.data != '*':
            min_val = min(int(root.left.data), int(root.right.data))
            root.right.data = int(root.right.data) - min_val
            root.left.data = int(root.left.data) - min_val
            root.data = min_val
        return root

result = 0

def sumResult(root):
    global result
    if root:
        sumResult(root.left)
        result += int(root.data)
        sumResult(root.right)
        return result

T = PerfectTree()

inp = input("Enter Input : ").split('/')
lst = inp[1].split()

# Check if the input list length is correct
if len(lst) != (int(inp[0]) // 2) + 1:
    print("Incorrect Input")
else:
    # Fill in missing values with '*'
    while len(lst) != int(inp[0]):
        lst.insert(0, '*')

    root = None

    # Insert values into the perfect binary tree
    for i in lst:
        root = T.insert(root, i)

    newRoot = checkTree(root)
    print(sumResult(newRoot))
