# Chapter : 10 - item : 2 - longest increasing subsequence
# แสดงค่าจำนวนตัวเลขมากที่สุด ที่สามารถเรียงจากน้อยไปมากได้โดยไม่สลับตำแหน่ง
class Queue:
    def __init__(self) -> None:
        self.data = []
    def enQueue(self, data):
        self.data.append(data)
    def deQueue(self):
        return self.data.pop(0)
    def size(self):
        return len(self.data)
    def __str__(self) -> str:
        return " ".join(self.data)

def find_next(data, number):
    for i in range(len(data)):
        if data[i] >= number:
            return i
    return len(data)


def long_inc_sub(arr):
    data = []
    temp = []
    for number in arr :
        if not temp or number > temp[-1]:
            temp.append(number)
            data.append(temp.copy())
        elif number <= temp[-1]:
            temp = temp[:find_next(temp, number)]
            temp.append(number)
            data.append(temp.copy())        
    
    for i in range(len(data)):
        print(f"{i+1} : {data[i]}")
    print(f"longest increasing subsequence : {max([len(i) for i in data])}")
        
    

inp = input("Data : ").split(" ")
inp = list(map(int, inp))
long_inc_sub(inp)
