# Chapter : 3 - item : 2 - Number in Stack

# จงสร้างฟังก์ชัน ManageStack() ในการจัดการตัวเลขที่อยู่ใน Stack โดยที่จะมีคำสั่งดังนี้

# A (add) : ทำการเพิ่มตัวเลขเข้าไปใน Stack

# P (pop) : ทำการนำเลขสุดท้ายใน Stack ออก ( ถ้า Stack ว่างให้แสดงผล -1 )

# D (delete) : ทำการลบตัวเลขที่ต้องการใน Stack ( ถ้า Stack ว่างให้แสดงผล -1 )

# LD (lessthan delete) : ทำการลบตัวเลขที่น้อยกว่าตัวเลขที่กำหนดทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )

# MD (Morethan delete) : ทำการลบตัวเลขที่มากกว่าตัวเลขที่ต้องการทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )

# การ Delete ทุกแบบ ถ้าหากไม่มีเลขที่ถูกลบเลย ไม่ต้องแสดงผลอะไรและให้ทำการแสดงผลค่าที่อยู่ใน Stack เมื่อจบโปรแกรม

# *** Hint ***

# ฟังก์ชัน Delete ต่างๆให้สร้าง Stack ขึ้นมาอีก 1 อันเพื่อใช้เป็น Temp ในการเก็บค่าตัวเลขต่างๆ

class Stack:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def __str__(self) -> str:
        s = f"stack of {str(self.size())} items :"
        for element in self.items:
            s += f"{str(element)} "
        return s

    def push(self, item):

        self.items.append(item)
        return item

    def pop(self):
        try:
            return self.items.pop()
        except:
            return -1

    def peek(self):
        try:
            return self.items[-1]
        except:
            return -1

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def deleted(self, item):
        try:
            self.items.remove(item)
            return item
        except:
            return -1


def ManageStack(opt):
    s1 = Stack()
    for char in opt:
        if char[0] == "A":
            print(f"Add = {s1.push(int(char.split(' ')[1]))}")
        elif char[0] == "P":
            print(f"Pop = {s1.pop()}")
        elif char[0] == "D":
            print(f"Delete = {s1.deleted(int(char.split(' ')[1]))}")
        elif char[:2] == "LD" :
            print(f"Less than Delete = {s1.deleted(int(char.split(' ')[1]))}")


text = input("Enter Input : ").split(",")
ManageStack(text)
