# Chapter : 4 - item : 3 - code with queue

# รับ string มาเข้าคิวหา secret code โดยรับ input คือ

# code เป็น string ยาว

# hint คือตัวแรกของรหัสที่ถูกต้อง

# **คำใบ้**

# ascii ของ "f" มีค่า = 102

# ascii ของ "g" มีค่า = 103

# ascii ของ "h" มีค่า = 104

# ascii ของ "i" มีค่า = 105

# ascii ของ "j" มีค่า = 106


class Queue:
    def __init__(self, items = None):
        if items is None:
            self.items = []
        else :
            self.items = items
    def enQueue(self , items ):
        self.items.append(items)
        return items
    def deQueue(self):
        return self.items.pop(0)
    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def __str__(self) -> str:
        return f"{self.items}"
    

q = Queue()
txt = input("Enter code,hint : ").split(',')
diff  =  ord(txt[0][0])  - ord(txt[1][0])

for char in txt[0]:
    if char:
        q.enQueue(chr(ord(char)-diff))
        print(q)
