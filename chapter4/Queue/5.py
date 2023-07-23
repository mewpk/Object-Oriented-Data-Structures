# Chapter : 4 - item : 5 - Search Portal

# พี่ซันฟงได้รับคำสั่งจากอาจารย์ให้ออกโจทย์เขียนโปรแกรมให้แก่น้องๆ พี่จึงกลับไปนอนคิดที่บ้าน รู้สึกตัวอีกทีก็อยู่ในห้องมืดๆ พี่สามารถมองเห็นและเดินไปยังพื้นที่ที่อยู่ติดกันได้ (4 ทิศ เหนือ ใต้ ออก ตก) พี่จะต้องหาประตูทางออกจากฝันเพื่อไปส่งโจทย์ให้กับอาจารย์ ต่อมาพี่ก็คิดวิธีในการเดินหาประตูทางออกได้โดยใช้วิธีหาแบบ Breadth First Search โดยพี่จะเริ่มยืนในจุดเริ่มต้นแล้วมองหาและจำทางเริ่มจากทิศเหนือ ทิศตะวันออก ทิศใต้ ทิศตะวันตก ตามลำดับ แล้วเดินไปยังช่องถัดไปแล้วหาใหม่ ในเมื่อคิดวิธีออกแล้วพี่จึงต้องการโปรแกรมที่จะบอกพี่ว่าสามารถไปถึงทางออกได้หรือพี่จะต้องติดอยู่ในฝันไปตลอดกาล ปัญหาคือพี่ขี้เกียจเขียนโค้ด พี่เลยอยากให้น้องๆเขียนโค้ดให้พี่หน่อย เขียนสวยๆกะทัดรัด ไม่งั้นจะส่งกลับไปเขียนใหม่
# โดยรายละเอียดโปรแกรมจะมีดังนี้
# Input
# รับความกว้าง ความสูง และแผนที่ โดยแผนที่แต่ละบรรทัดจะขั้นด้วย ','
# ตัวอย่าง input: 3 3 F__,##_,O__
# จะมีความหมายว่าแผนที่กว้าง 3 สูง 3 และแผนที่จะเป็นแบบนี้
# F__
# ##_
# O__
# ภายในแผนที่
# 'F' แทนตำแหน่งเริ่มต้นของพี่
# 'O' แทนประตูทางออก
# '_' แทนพื้นที่ที่สามารถเดินได้
# ตัวอักษรอื่นๆทั้งหมดแทนกำแพง ไม่สามารถเดินไปที่ช่องนั้นได้
# Output
# หากไม่มีพี่ (F) อยู่ในห้องหรือแผนที่ที่ใส่เข้ามาไม่ตรงกับขนาดของ width ให้แสดงว่า "Invalid map input."
# แสดง queue ระหว่างหาทางออก
# ถ้าหาทางออกเจอให้แสดงว่า "Found the exit portal."
# ถ้าหาไม่เจอให้แสดงว่า "Cannot reach the exit portal."

class Queue :
    def __init__(self, items=None):
        if items :
            self.items = items
        else :
            self.items = []
    def deQueue(self):
        if self.isEmpty() :
            return -1
        return self.items.pop(0)
    def enQueue(self,item):
        self.items.append(item)
        return item
    def isEmpty(self):
        return len(self.items) == 0 
    def size(self):
        return len(self.items)
    
    