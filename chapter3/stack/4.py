# Chapter : 3 - item : 4 - Stack Calculator

# ให้เขียน class calculator  ที่มีการทำงานผ่านฟังก์ชัน run(instructions) โดยมี instructions ดังนี้
# +: Pop 2 ค่าออกจาก stack, นำมาบวกกัน และ push ผลลัพธ์ลง stack
# -: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนลบด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
# *: Pop 2 ค่าออกจาก stack, นำมาคูณกัน และ push ผลลัพธ์ลง stack
# /: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนหารด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
# DUP: Duplicate (not double) ค่าบนสุดของ stack
# POP: Pop ค่าบนสุดออกจาก stack และ discard.
# PSH: ทำการ push ตัวเลขลง stack
# หมายเหตุ คำสั่งอื่น ๆ (เช่นตัวอักษร) ควรทำให้เกิดค่า "Invalid instruction: [instruction]"
# *************************************************
# print("* Stack Calculator *")
# arg = input("Enter arguments : ")
# machine = StackCalc()
# machine.run(arg)
# print(machine.getValue())

class StackCalc :
    def __init__(self , list = None):
        self.status = True
        if list == None :
            self.items = []
        else :
            self.items = list
    def __str__(self) -> str:
        s = f"stack of {str(self.size())} items :"
        for element in self.items :
            s += f"{str(element)} "
        return s
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        try :
           return self.items[-1]
        except :
            return 0
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def run(self,args):
        for arg in args:
            if arg.isdigit():
                self.push(int(arg))
            elif arg == "+":
                self.push(self.pop() + self.pop())
            elif arg == "-":
                self.push(self.pop() - self.pop())
            elif arg == "*":
                self.push(self.pop() * self.pop())
            elif arg == "/":
                self.push(int(self.pop() / self.pop() ))
            elif arg == "DUP" :
                if self.peek() != 0:
                    self.push(self.peek())
                    # print(self.peek())
            elif arg == "POP" :
                if self.peek()!= 0:
                    self.pop()
            else :
               print(f"Invalid instruction: {arg}")
               self.status = False
               break
        
    def getValue(self):
        return self.peek()



print("* Stack Calculator *")
arg = input("Enter arguments : ").split(" ")
machine = StackCalc()
machine.run(arg)
if machine.status :
    print(machine.getValue())