# Chapter : 9 - item : 1 - หัดใช้ Sort

# ให้น้องๆทำการตรวจสอบว่า input ที่เราใส่ลงไปนั้นได้มีการเรียงลำดับมาแล้วหรือไม่ 
# ถ้าหากเรียงมาแล้วให้แสดงผลเป็น Yes แต่ถ้าหากไม่ให้แสดงผลเป็น No

# ****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง

inp = list(map(int,input("Enter Input : ").split(" ")))

def sort(inp):
    while True:
        check = True
        for i in range(len(inp)-1):
            if inp[i] > inp[i+1]:
                inp[i], inp[i+1] = inp[i+1], inp[i]
                check = False
        if check:
            break
    return inp

if sort(inp.copy()) == inp:
    print("Yes")
else :
    print("No")