# Chapter : 12 - item : 5 - MyInt roman
# จงสร้าง class MyInt ซึ่งคลาสนี้เป็นคลาสที่เก็บเลขจำนวนเต็มโดยมี method ดังต่อไปนี้
# __init__ สำหรับสร้างคลาส โดยรับจำนวนเต็มเพื่อใช้เป็นตัวแปรในคลาส
# toRoman สำหรับเปลี่ยนค่าตัวเลขฐานสิบเป็นเลข Roman
# โดยตัวเลข Roman มีค่าดังนี้

# "M" = 1000
# "CM" = 900
# "D" = 500
# "CD" = 400
# "C" = 100
# "XC" = 90
# "L" = 50
# "XL" = 40
# "X" = 10
# "IX" = 9
# "V" = 5
# "IV" = 4
# "I" = 1
# __add__ สำหรับการบวกค่าตัวเลขของคลาสนี้เมื่อบวกแล้วจะเพิ่มค่าที่บวกอีกครึ่งหนึ่งของผลลัพธ์ที่ได้
# โดยมีการเรียกใช้งานดังนี้
# a = MyInt(500)
# b = MyInt(40)
# print(a.toRoman())
# print(b.toRoman())
# print(a+b)
# ผลลัพธ์
# D
# XL
# 810
# โดยให้เขียนโปรแกรมเพื่อรับค่า ตัวเลข 2 ตัว และแสดงผลดังตัวอย่าง



class MyInt:
    def __init__(self, number):
        self.number = number
        self.roman_dict = {"M": 1000,
                           "CM": 900,
                           "D": 500,
                           "CD": 400,
                           "C": 100,
                           "XC": 90,
                           "L": 50,
                           "XL": 40,
                           "X": 10,
                           "IX": 9,
                           "V": 5,
                           "IV": 4,
                           "I": 1
                           }

    def toRoman(self):
        temp_number = self.number
        roman = ""
        while temp_number > 0 :
            for key in self.roman_dict:
                if temp_number >= self.roman_dict[key]:
                    temp_number -= self.roman_dict[key]
                    roman += key
                    break
            else:
                break
        return f"{self.number} convert to Roman : {roman}"

    def __add__(self, other):
        new_number = self.number + other.number
        new_number += new_number/2
        return MyInt(int(new_number))

    def __str__(self) -> str:
        return f"{number1} + {number2} = {str(self.number)}"

print(" *** class MyInt ***")
number1, number2 = list(map(int,input("Enter 2 number : ").split(" ")))

a = MyInt(number1)

b = MyInt(number2)

print(a.toRoman())

print(b.toRoman())

print(a+b)
