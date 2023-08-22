# Chapter : 6 - item : 4 - Integer Partition

# พี่ซันฟงต้องการโจทย์ recursion ที่ทำให้น้องๆต้องกุมขมับแต่พี่ไม่มีไอเดียในหัวเลย 
#  แต่จู่ๆนักคณิตศาสตร์ในตัวพี่ก็ฉุดคิดอะไรขึ้นมาได้

# "วิธีการบวกเลขจำนวนเต็มมีกี่วิธี" นักคณิตศาสตร์ตั้งคำถามพร้อมนึกวิธีหาคำตอบ


# "ก็ต้องมีไม่จำกัดหรือเปล่า" พี่ตอบกลับไปหลังลองคิดวิธี "สมมุติเลข 0 ก็เกิดจาก 

# 1+(-1), 2+(-2) ไปเรื่อยๆ"

# "เราก็แค่กำหนดขอบเขตให้เป็นเลขจำนวนเต็มบวกสิ"

# "ถ้างั้นเลข 4 ก็จะต้องมีทั้งหมด 5 วิธีรวมตัวมันเองด้วย ก็จะมี 4, 3+1, 2+2, 2+1+1, 1+1+1+1"


# "ใช่ ต่อไปก็แค่คิด algorithm ขึ้นมา"

# "มันดูคล้ายๆกับการหา combinations อยู่นะเนี่ย" ทันทีที่พี่พูดจบพี่ก็เริ่มไปหาข้อมูลในอินเตอร์เน็ตก็พบว่า
#  พี่ไม่ได้คิดขึ้นมาได้เป็นคนแรก และการหาวิธีการหาผลรวมนี้เรียกว่า integer partition 
#  พี่ได้ข้อมูลมาจาก link นี้

# https://en.m.wikipedia.org/wiki/Partition_(number_theory)

# เป็นการหาจำนวนวิธีที่แตกต่างกันของการรวมเลขจำนวนเต็มบวกให้เท่ากับ n (เลขจำนวนเต็มไม่ติดลบ)

# โจทย์มีอยู่ว่าให้เขียนโปรแกรมที่รับเลขสองตัว

# ตัวแรก n เลขที่ต้องการหาวิธีในการบวก

# ตัวที่สอง s คือจำนวนบรรทัดที่แสดงวิธีการบวก และแสดง ". . ." ครั้งเดียวสำหรับบรรทัดที่เหลือ

# Output ให้แสดงวิธีในการบวก และจำนวนวิธีในการบวกทั้งหมด

# ห้ามใช้ for loop ไม่มีข้อยกเว้น

# n ∈ {0, 1, 2, ...}

# s ∈ {0, 1, 2, ...}




# list_integer_partition = []

# def integer_partition(start, cur, cur_list):
#     global n,s    
#     if cur <= 0:
#         return
#     new_list = cur_list.copy()
#     new_list.append(cur)
#     print("check" , new_list)

#     if sum(new_list) == n:
#         if new_list not in list_integer_partition:
#             s -= 1
#             if s >= 0 :
#                 print(" + ".join(list(map(str,reversed( sorted(new_list))))))
#             list_integer_partition.append(new_list)
#     elif sum(new_list) > n:
#         integer_partition(start, cur - 1, cur_list)
#         return

#     integer_partition(start, cur, new_list)
#     integer_partition(start, cur - 1, cur_list)
    

# def loop_integer(n):
    
#     if n == 0:
#         return
#     integer_partition(n, n, [])
#     loop_integer(n - 1)

# n, s = input("Enter n, s: ").split(" ")
# n ,s = int(n) , int(s)
# temp_s = s
# if n == 0 and s > 0:
#     print(0)
#     list_integer_partition.append([0])
# if n >= 0 and s >= 0 :
#     loop_integer(n)
#     list_integer_partition.sort()
#     if len(list_integer_partition) > temp_s :
#         print(". . .")
#     print("Total:", len(list_integer_partition))

def integer_partition(n, max_value, path=[]):
    global s,num
    if n == 0:
        s -= 1
        if s >= 0 :
            if num == 0 :
                print(0)
            else :
                print(" + ".join(map(str, path)))
        return 1
    if n < 0 or max_value == 0:
        return 0
    
    count = 0
    count += integer_partition(n - max_value, max_value, path + [max_value])
    count += integer_partition(n, max_value - 1, path)
    
    return count

num, s = map(int, input("Enter n, s: ").split())

temp_s = s

partitions_count = integer_partition(num, num)
# if num == 0 and partitions_count > temp_s:
    # print(0)
if temp_s < partitions_count:
    print(". . .")

print("Total:", partitions_count)
