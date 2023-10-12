# Chapter : 10 - item : 4 - Isomorphic string
# วันนี้เป็นวันเกิดพี่ฟง (3 ต.ค.) ดังนั้นพี่จึงจะแจกของขวัญให้น้องๆ
# ถ้ากำหนดให้ชื่อน้องๆและชื่อของขวัญแทนด้วยตัวอักษร 1 ตัว
# ช่วยหาว่าพี่ฟงจะสามารถให้ของขวัญน้องๆคนละชิ้นโดยที่ไม้ให้ของซ้ำกันได้หรือไม่
# รูปแบบ input: str1,str2
# Expected Complexity: O(n)
# ห้ามใช้ dict set อยากใช้ทำเอง
# ตัวอย่าง
# รายชื่อน้อง (str1): ACAB
# รายชื่อของ (str2): XCXY
# เป็น Isomorphic เพราะ A -> X, C -> C, B -> Y
# ตัวอย่าง 2
# str1: ABAB
# str2: XCXY
# ไม่เป็น Isomorphic เพราะ A -> X แต่ B -> C และ B -> Y
# ตัวอย่าง 3
# str1: ACAB
# str2: XCXC
# ไม่เป็น Isomorphic เพราะ A -> X แต่ C -> C และ B -> C

def are_isomorphic(str1, str2):
    
    if len(str1) != len(str2):
        return False

    mapping1 = [-1] * 128  
    mapping2 = [-1] * 128

    for i in range(len(str1)):
        char1 = ord(str1[i])
        char2 = ord(str2[i])

        if mapping1[char1] == -1:
            mapping1[char1] = char2

        if mapping2[char2] == -1:
            mapping2[char2] = char1

        if mapping1[char1] != char2 or mapping2[char2] != char1:
            return False

    return True

str1, str2 = input("Enter str1,str2: ").split(",")

if are_isomorphic(str1, str2):
    print(f"{str1} and {str2} are Isomorphic")
else:
    print(f"{str1} and {str2} are not Isomorphic")
