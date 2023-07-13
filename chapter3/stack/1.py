# Chapter : 3 - item : 1 - Parentheses ver.1
# ให้น้องๆเขียนโปรแกรมรับ input เป็นวงเล็บ โดยมีรูปแบบดังนี้  
# วงเล็บเปิด :  (  กับ  [    วงเล็บปิด :  )  กับ  ]   โดยให้หาว่าถ้าหากนำวงเล็บมาจับคู่กัน จะครบทุกคู่หรือไม่ 
#  โดยให้แสดงผลลัพธ์ออกมาเป็นจำนวนวงเล็บที่จะต้องเติมหากวงเล็บมีไม่ครบคู่   แต่ถ้าหากครบคู่ให้แสดงคำว่า  Perfect  ออกมาด้วย

class Stack :
    def __init__(self , list = None):
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
    
def parentheses(str) :
    s1  = Stack()
    count = 0
    for i in range(0, len(str)):
        if str[i] == "("  or str[i] == "[":
            s1.push(str[i])
            count += 1
        elif (str[i] == "]" and s1.peek() == "[") or (str[i] == ")" and s1.peek() == "("):
            s1.pop()
            count -=1
        else :
            count += 1
    
    return count
text  = list(input("Enter Input : "))


count = parentheses(text)
print(count)
if count == 0 :
    print("Perfect ! ! !")



