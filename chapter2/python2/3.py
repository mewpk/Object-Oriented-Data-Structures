# Chapter : 2 - item : 3 - Mod Position

# ให้นักศึกษาเขียนโปรแกรมภาษา Python โดยใช้ Function ในการแสดงตำแหน่งของ List ในตำแหน่งที่หารเลขใดๆลงตัว จาก String

# def mod_position(arr, s):
#     //Code Here

# Input ตำแหน่งที่แรกเป็นค่าใน String ที่นำเข้ามา
# Input ตำแหน่งที่สองเป็นตัวเลขที่ทำการบอกว่าจะแสดงที่ตำแหน่งที่หารตัวเลขนั้นๆลงตัว เช่นถ้าใส่เลข 3 และ String มีค่าเป็น ABCDEFG ก็จะแสดงตำแหน่งที่ 3 คือ C กับตำแหน่งที่ 6 คือ 


print("*** Mod Position ***")

def mod_position(arr, s):
    temp = []

    for i in range(1,len(arr)+1):
        if i % int(s) == 0:
            temp.append(arr[i-1])
    return temp


arr,s = input("Enter Input : ").split(",")
print(mod_position(arr, s))