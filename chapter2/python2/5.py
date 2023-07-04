# Chapter : 2 - item : 5 - funString

# จงสร้าง Class funString ที่จะรับพารามิเตอร์เป็น String และเลขคำสั่งโดยมีฟังก์ชันดังต่อไปนี้

# 1. หาความยาวของ String

# 2. สลับพิมพ์เล็กพิมพ์ใหญ่ใน String (ห้ามใช้คำสั่ง upper และ lower)

# 3. Reverse String (ห้ามใช้คำสั่ง reversed)

# 4. ลบตัวอักษรที่ปรากฏมาก่อนใน String



# class funString():

#     def __init__(self,string = ""):

#         ### Enter Your Code Here ###

#     def __str__(self):

#         ### Enter Your Code Here ###

#     def size(self) :

#         ### Enter Your Code Here ###

#     def changeSize(self):

#         ### Enter Your Code Here ###

#     def reverse(self):

#         ### Enter Your Code Here ###

#     def deleteSame(self):

#        ### Enter Your Code Here ###



# str1,str2 = input("Enter String and Number of Function : ").split()

# res = funString(str1)

# if str2 == "1" :    print(res.size())

# elif str2 == "2":  print(res.changeSize())

# elif str2 == "3" : print(res.reverse())

# elif str2 == "4" : print(res.deleteSame())









class funString():
    
    def __init__(self,string = ""):

        ### Enter Your Code Here ###
        self.string = string

    def __str__(self):

        ### Enter Your Code Here ###
        return self.string

    def size(self) :

        ### Enter Your Code Here ###
        return len(self.string)

    def changeSize(self):

        ### Enter Your Code Here ###
        return self.string.swapcase()

    def reverse(self):

        ### Enter Your Code Here ###
        return self.string[::-1]
    def deleteSame(self):
        
       ### Enter Your Code Here ###
        temp = []
        for i in list(self.string):
            if i not in temp:
                temp.append(i)
        return ''.join(temp)


str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :    print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())