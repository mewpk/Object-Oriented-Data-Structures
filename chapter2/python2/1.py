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