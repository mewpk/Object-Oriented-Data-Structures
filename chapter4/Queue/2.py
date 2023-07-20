# Chapter : 4 - item : 2 - PSD48 a.k.a เขาเรียกผมว่าเอเรน

# PSD48 (P-Saderd 48 Group) เป็นวงไอดอลวงหนึ่งที่กระแสกำลังมาแรง ณ ตอนนี้โดยเพลงที่ได้รับความนิยมอย่างมากคือเพลงจี่หอย โดยวง PSD48 
# กำลังจะจัดงานจับมือขึ้น 
# โดยมีกฎอยู่ว่าถ้าหากคนที่กำลังต่อแถวอยู่เป็นคนจาก กองกำลังสำรวจ จะได้สิทธิพิเศษในการแทรกแถวไปข้างหน้าสุดทันที 
#(แต่ถ้าหากคนหน้าสุดก็เป็นคนของกองกำลังสำรวจก็ต้องต่อหลังเขาอยู่ดี)  PSD48 อยากให้คุณช่วยเขียนโปรแกรมสำหรับหาว่าจะมีโอตะ id ใดบ้างที่ได้จับมือ

# เพลงประกอบ : https://youtu.be/Jd4Hd-HFgls

# Input :
# EN <value>  เป็นโอตะธรรมดา  id = value
# ES <value>  เป็นโอตะของกองกำลังสำรวจ  id = value
# D                  เป็นคำสั่งแสดงผล value ของหัวแถว ถ้าหากในแถวไม่มีคนจะแสดงคำว่า Empty

class Queue :
    def __init__(self,items=None):
        if items is None:
            self.items = []
        else :
            self.items = items
    def enQueue(self,i):
        self.items.append(i)
        return i
    def deQueue(self):
        return self.items.pop(0)
    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def __str__(self) -> str:
        return f"{self.items}"

q1 = Queue()
q2 = Queue()
text = input("Enter Input : ").split(",")

for char in text:
    opt = char.split(" ")
    if opt[0] == "EN" :
        q1.enQueue(opt[1])
    elif opt[0] == "ES" :
        q2.enQueue(opt[1])
    elif opt[0] == "D":
        if not q2.isEmpty():
            print(q2.deQueue())
        elif not q1.isEmpty():
            print(q1.deQueue())
        else :
            print("Empty")