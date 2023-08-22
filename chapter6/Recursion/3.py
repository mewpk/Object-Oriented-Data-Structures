# Chapter : 6 - item : 3 - เคโรโระ
 
# เคโรโระ

# กบเขียวเคโรโระ ต้องการกระโดดจากช่องหมายเลข 0 ไปเลขต่างๆ ไม่เกิน 40 เคโรโระ
#  ต้องการทราบวิธีการไปทั้งหมด และจำนวนครั้งที่กระโดดน้อยที่สุด เมื่อเคโรโระสามารถกระโดดได้ทีละ 1 5 7 ช่อง

# เช่น ไปช่อง 7 จะมี 5 วิธีคือ

# โดด 7 ครั้ง 1 1 1 1 1 1 1

# โดด 3 ครั้ง  5 1 1

# โดด 3 ครั้ง  1 5 1

# โดด 3 ครั้ง  1 1 5

# โดด 1 ครั้ง  7  น้อยสุด

# ไปช่อง 7 จะมี 5 วิธี โดดน้อยสุด 1

# แต่ว่ากบแดงกิโรโระจะดักโจมตีช่องที่หารด้วย14ลงตัว ทำให้เคโรโระไม่สามารถผ่านช่องเหล่านั้นได้ 
# ถ้าเคโรโระไม่สามารถไปถึงจุดหมายได้ ให้แสดง mission failed

list_distance = []

def keroro(n,count,final):
    count += 1
    # print(n)
    if n % 14 == 0 and n != 0 :
        return
    if n == final :
        list_distance.append(count)
        return
    elif n > final :
        return
    keroro(n+1,count,final)
    keroro(n+5,count,final)
    keroro(n+7,count,final)

n = int(input("Input number : "))
keroro(0,-1,n)
if (len(list_distance) > 0):
    print(f"Minimum Distance is {min(list_distance)}")
    print(f"Maximum Way is {len(list_distance)}")
else :
    print("Mission Failed")