# Chapter : 2 - item : 1 - Simple OOP Calculator

# จงเขียน Overloading Function สำหรับ Calculator class โดยที่มีรูปแบบ Code ดังนี้ (สามารถเพิ่มพารามิเตอร์ได้)
# class Calculator :
#     ### Enter Your Code Here ###
#     def __add__(self):
#         ###Enter Your Code For Add Number###
#     def __sub__(self):
#         ###Enter Your Code For Sub Number### 
#     def __mul__(self):
#         ###Enter Your Code For Mul Number###
#     def __truediv__(self):
#         ###Enter Your Code For Div Number###
# x,y = input("Enter num1 num2 : ").split(",")
# x,y = Calculator(int(x)),Calculator(int(y))
# print(x+y,x-y,x*y,x/y,sep = "\n")


class Calculator :

    ### Enter Your Code Here ###
    def __init__(self,number):
        self.number = number
    def __add__(self,other):
        ###Enter Your Code For Add Number###
        return self.number + other.number

    def __sub__(self,other):

        ###Enter Your Code For Sub Number### 
        return self.number - other.number
    def __mul__(self,other):

        ###Enter Your Code For Mul Number###
        return self.number * other.number
    def __truediv__(self,other):

        ###Enter Your Code For Div Number###
        return self.number / other.number

x,y = input("Enter num1 num2 : ").split(",")

x,y = Calculator(int(x)),Calculator(int(y))

print(x+y,x-y,x*y,x/y,sep = "\n")