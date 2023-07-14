# Chapter : 3 - item : 3 - Infix to Postfix
# ให้รับ Input เป็น  Infix  และแสดงผลลัพธ์ออกมาเป็น  Postfix   โดยจะมี Operator  5  แบบ  ได้แก่  +   -   *   /   ^

# class Stack:

#     def __init__(self):

#     def push(self, value):

#     def pop(self):

#     def size(self):

#     def isEmpty(self):

# inp = input('Enter Infix : ')

# S = Stack()

# print('Postfix : ', end='')

# ### Enter Your Code Here ###

# while not S.isEmpty():

#     print(S.pop(), end='')

# print()

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
            return -1
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)


inp = input('Enter Infix : ')

S = Stack()

print('Postfix : ', end='')

### Enter Your Code Here ###

operator = {
    "(" : 0,
    "+" : 1,
    "-" : 1,
    "/" : 2,
    "*" : 2,
    "^" : 4,
}


for i in range(len(inp)):
    
    opt = inp[i]
    if opt not in operator and opt != ")" :
        print(opt, end='')
    else :
        if opt == ")" :
            while S.peek() != "(" :
                if S.peek() != -1 :
                    print(S.pop(), end='')
                else :
                    break
            if S.peek() != -1 :
                S.pop()
        elif S.peek() not in operator :
            S.push(opt)
        else :
            if S.peek() != -1 :
                if operator[S.peek()] <= operator[opt] :
                    S.push(opt)
                else :
                    # while True :
                    #     if S.peek() in operator and operator[S.peek()] > operator[opt]:
                    #         print(S.pop(), end='')
                    #     else :
                    #         break
                    for i in range(S.size()):
                        print(S.pop(), end='')
                    S.push(opt)


for i in range(S.size()) :
    print(S.pop(), end='')
print()