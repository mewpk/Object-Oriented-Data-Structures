# เขียนโปรแกรมที่แสดงผลดังตัวอย่าง

# ****ห้ามใช้คำสั่ง for, while, do while*****

# หมายเหตุ ฟังก์ชันมี parameter ได้ไม่เกิน 2 ตัว

# def staircase(n):
#     #code here

# print(staircase(int(input("Enter Input : "))))    Enter Input : 3
# __#
# _##
# ###
#       Enter Input : -8
# ########
# _#######
# __######
# ___#####
# ____####
# _____###
# ______##
# _______#

count = 1
def staircase(n):
    global count
    if n > 0 :
        print("_"*(n-1),"#"*count , sep="")
        count += 1
        staircase(n-1)
    elif n < 0 :
        print("_"*(count-1),"#"*(-n) , sep="")
        count += 1
        staircase(n+1)
    else :
        return
staircase(int(input("Enter Input : ")))