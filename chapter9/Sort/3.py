# Chapter : 9 - item : 3 - somethingDROME
# รับจำนวนเต็มมา 1 จำนวนแล้วให้แสดงผลดังนี้

# - หาก input ที่รับมานั้นมีการเรียงลำดับจากน้อยไปมาก และไม่มีตัวซ้ำเลยให้แสดงผลว่า "Metadrome"

# - หาก input ที่รับมานั้นมีการเรียงลำดับจากน้อยไปมาก และมีตัวซ้ำให้แสดงผลว่า "Plaindrome"

# - หาก input ที่รับมานั้นมีการเรียงลำดับจากมากไปน้อย และไม่มีตัวซ้ำเลยให้แสดงผลว่า "Katadrome"

# - หาก input ที่รับมานั้นมีการเรียงลำดับจากมากไปน้อย และมีตัวซ้ำให้แสดงผลว่า "Nialpdrome"

# - หาก input ที่รับมานั้นทุกหลักเป็นเลขเดียวกันหมด ให้แสดงผลว่า "Repdrome"

# - หากไม่อยู่ในเงื่อนไขด้านบนเลย ให้แสดงผลว่า "Nondrome"

# ****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง

inp = list(map(int,input("Enter Input : ")))

def sort(inp):
    while True :
        check = True
        for i in range(len(inp)-1):
            if inp[i] > inp[i+1]:
                inp[i], inp[i+1] = inp[i+1], inp[i]
                check = False
        if check:
            break
    return inp

if len(set(inp)) == 1:
    print("Repdrome")
elif inp == sort(inp.copy()) and len(inp) == len(set(inp)):
    print("Metadrome")
elif inp == sort(inp.copy()) and len(inp) != len(set(inp)):
    print("Plaindrome")
elif inp == sort(inp.copy())[::-1] and len(inp) == len(set(inp)):
    print("Katadrome") 
elif inp == sort(inp.copy())[::-1] and len(inp) != len(set(inp)):
    print("Nialpdrome")
else :
    print("Nondrome")





