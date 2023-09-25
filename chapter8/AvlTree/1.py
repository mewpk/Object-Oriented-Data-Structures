# Chapter : 8 - item : 1 - AVL Tree มันทำยาก เผามันเลยละกัน

# พี่ว่าการสร้าง Tree มันยากเกินไปและใช้เวลานานมาก กว่าต้นไม้จะโต 
# เพราะฉะนั้นเราจะทำอะไรให้มันเร็วกว่าการปลูกต้นไม้ดีกว่า นั่นคือการ เผามันเลย ยังไงล่ะ

# โดยที่เดี๋ยวพี่จะจุดไฟใส่ กิ่ง หรือ ใบไม้สักใบนึง แล้วดูว่าพอเวลาผ่านไปทุกๆนาที 
# จะมีส่วนไหนของต้นไม้บ้างที่ไหม้เกรียมไปแล้วบ้าง

# หลักการทำงานคร่าวๆ
# สร้าง AVL Tree ด้วยความตั้งใจ (ตัวแรกไม่จำเป็นต้องเป็น Root เสมอไป)
# จุดไฟที่ node นั้น -> ถือว่า node นั้นไหม้ไปแล้ว
# ทุกๆนาที จะมี กิ่ง หรือ ใบ รอบๆข้างที่เชื่อมต่อกับ node นั้นไหม้ทั้งหมด
# โดยให้วนดูจาก left child node ของ node นั้นก่อนเสมอ
# ตามด้วย right child node
# ปิดท้ายด้วย parent node ของ node นั้น
# ถ้าไม่มี node ที่อยู่ติดกับ node ที่ไหม้ไปแล้ว ก็ปล่อยมันไป
# บอกพี่หน่อยว่า แต่ละนาที มี node ไหนที่ไหม้ไปบ้าง

# เช่น Testcase #1 : Node ที่จะเผาคือ Node(14)

#              14

#     12            21

# 10     13   15       23

#                         22 24

# Minute 0 : 14 (เผาอยู่)

# Minute 1 : 12 21 (ไฟลามไปทาง left child node แล้วค่อยไป right child node)

# Minute 2 : 10 13 15 23 (ไฟลามเหมือนเดิม วนไป)

# Minute 3 : 22 24 (Node(10), Node(13) ไม่มีตัวต่อแล้ว ก็ไม่ต้องสนอะไร
#  ไฟลามไป child ของ node ที่เหลือแทน)

# **************************************************
# พี่ ญ่า ตั้งใจออกข้อนี้มากเลยนะขอให้น้องๆตั้งใจทำนะ
# **************************************************
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = self.right = None
        self.height = 1  # Initialize the height to 1 for new nodes.

    def __str__(self):
        return str(self.data)


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root = self._insert(data, self.root)

    def _insert(self, data, root):
        if data < root.data:
            if root.left is None:
                root.left = Node(data)
            else:
                root.left = self._insert(data, root.left)
        else:
            if root.right is None:
                root.right = Node(data)
            else:
                root.right = self._insert(data, root.right)

        # Update the height of the current node.
        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        # Perform rebalancing after insertion.
        return self._balance(data, root)

    def _get_height(self, node):
        if node is None:
            return 0
        return node.height

    def _balance_factor(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _balance(self, data, node):
        balance_factor = self._balance_factor(node)

        # Left Heavy
        if balance_factor > 1:
            # Left-Left Case
            if data < node.left.data:
                return self._rotate_right(node)
            # Left-Right Case
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

        # Right Heavy
        if balance_factor < -1:
            # Right-Right Case
            if data > node.right.data:
                return self._rotate_left(node)
            # Right-Left Case
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

    def _rotate_left(self, node):
        # Perform a left rotation on the node.
        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        # Update heights after rotation.
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        new_root.height = 1 + max(self._get_height(new_root.left), self._get_height(new_root.right))

        return new_root

    def _rotate_right(self, node):
        # Perform a right rotation on the node.
        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        # Update heights after rotation.
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        new_root.height = 1 + max(self._get_height(new_root.left), self._get_height(new_root.right))

        return new_root

    def printTree(self, node, level=0):
        if node is not None:
            # Print the right subtree, the node itself, and then the left subtree.
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def findNode(self,data , node):
        global count , burnNode
        if data == node.data:
            return [node , node.left , node.right]
        elif node.left == node.right == None or node == None:
            return False
        elif node.left and data == node.left.data:
            return [node.left , node.left.left, node.left.right , node]
        elif node.right and data == node.right.data:
            return [node.right , node.right.left, node.right.right , node]
        else :
            if data < node.data :
                return self.findNode(data , node.left)
            else :
                return self.findNode(data , node.right)
class Queue:
    def __init__(self) -> None:
        self.items = []

    def enQueue(self, item):
        self.items.append(item)

    def deQueue(self):
        return self.items.pop(0)



# Create an AVL tree instance.
tree = AVLTree()

# Collection Burn Node
burnNode = []
stepBurn = []
temp = []
check = True
again = 0
# Size of Tree
size = 1

# Queue
q = Queue()

# count 
count = -1

# Input data from the user.
data = input("Enter node and burn node : ").split()
for e in data[:-1]:
    size += 1
    tree.insert(int(e))
tree.insert(int(data[-1].split("/")[0]))


startBurn = int(data[-1].split("/")[1])

# Print the AVL tree.
# tree.printTree(tree.root)

# print(tree.findNode(startBurn, tree.root))


# Check Start Burn
if not tree.findNode(startBurn, tree.root) :
    print(f"There is no {startBurn} in the tree.")
# Burn Node
else :
    for i in range(size) :
        if not check :
            count = 0
        temp = []
        if again > 1:
            for i in range(again-1):
                if len(q.items) > 0 :
                    startBurn = q.deQueue()
                for item in tree.findNode(startBurn, tree.root) : 
                    if item and item not in burnNode :
                        count += 1
                        temp.append(item.data)
                        burnNode.append(item)
                        q.enQueue(item.data)
            again = 0
        if len(q.items) > 0 :
            startBurn = q.deQueue()
        for item in tree.findNode(startBurn, tree.root) : 
            if item and item not in burnNode :
                count += 1
                temp.append(item.data)
                burnNode.append(item)
                q.enQueue(item.data)
        if count > 1 :
            again = count
            stepBurn.append(list(map(str,temp)))
            temp = []
        elif count <= 1 and temp != [] :
            stepBurn.append(list(map(str,temp)))
        if check :
            q.deQueue()
        check = False
print(stepBurn[0].pop(0))
for i in stepBurn :
    print(" ".join(i))