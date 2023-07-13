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
        return f"Value in Stack = {list(self.items)}"

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
            test = - 1
            s2 = Stack()
            for i  in range(0, self.size()):
                if self.peek() == item:
                    self.pop()
                    print(f"Delete = {item}")
                    test = 1
                else :
                    s2.push(self.pop())
            for i in range(s2.size()):
                self.push(s2.pop())
            return test
        except:
            return -1
    def LD(self,number):
        try:
            s2 = Stack()
            test = -1
            for i  in range(0, self.size()):
                if self.peek() < number:
                    check = self.pop()
                    test = 1
                    print(f"Delete = {check} Because {check} is less than {number}")
                else :
                    s2.push(self.pop())
            for i in range(s2.size()):
                self.push(s2.pop())
            return test
        except:
            return -1
    def MD(self,number):
        try:
            s2 = Stack()
            test = -1
            for i  in range(0, self.size()):
                if self.peek() > number:
                    check = self.pop()
                    test = 1
                    print(f"Delete = {check} Because {check} is more than {number}")
                else :
                    s2.push(self.pop())
            for i in range(s2.size()):
                self.push(s2.pop())
            return test
        except:
            return -1


def ManageStack(opt):
    s1 = Stack()
    for char in opt:
        if char[0] == "A":
            print(f"Add = {s1.push(int(char.split(' ')[1]))}")
        elif char[0] == "P":
            if s1.peek() == -1 :
                print(-1)
            else :
                print(f"Pop = {s1.pop()}")
        elif char[0] == "D":
            if s1.deleted(int(char.split(' ')[1])) == -1 and s1.peek() == -1 :
                print(-1)
                
        elif char[:2] == "LD" :
            if s1.LD(int(char.split(' ')[1])) == -1  and s1.peek() == -1:
                print(-1)
        elif char[:2] == "MD" :
            if s1.MD(int(char.split(' ')[1])) == -1 and s1.peek() == -1 :
                print(-1)

    print(s1)

text = input("Enter Input : ").split(",")
ManageStack(text)

