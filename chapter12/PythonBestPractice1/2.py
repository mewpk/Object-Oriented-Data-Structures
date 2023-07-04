# Chapter : 12 - item : 2 - ตัวประกอบ

# รับจำนวนเต็มบวก 1 จำนวนแล้วหาว่า มีจำนวนที่หารลงตัวกี่จำนวน โดยให้แสดงผลเหมือนตัวอย่าง

print(" *** Divisible number ***")
number = int(input("Enter a positive number : "))
if number <= 0:
    print(f"{number} is OUT of range !!!")
else : 
    list = []
    for i in range(1, number + 1):
        if number % i == 0:
            list.append(i)
    print(f"Output ==> {' '.join(map(str,list))}")
    print(f"Total ==> {len(list)}")
