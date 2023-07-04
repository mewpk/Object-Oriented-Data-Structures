# Chapter : 2 - item : 4 - 3 SUM(2)

# จงเขียนฟังก์ชันเพื่อหาผลรวมของ 3 พจน์ใดๆใน Array ที่มีผลรวมเท่ากับ 5 สำหรับ Array ที่มีข้อมูลข้างในเป็นจำนวนจริง ***Array ต้องมีความยาวตั้งแต่ 3 จำนวนขึ้นไป*

list_number = list(map(int, input("Enter Your List : ").split(" ")))

result = []
if len(list_number) >= 3:
    list_number.sort()
    for i in range(len(list_number)-2):
        for j in range(i+1, len(list_number)-1):
            for k in range(j+1, len(list_number)):
                if list_number[i] + list_number[j] + list_number[k] == 5:
                    temp = [list_number[i], list_number[j], list_number[k]]
                    check = True
                    for res in result:
                        if sorted(res) == sorted(temp):
                            check = False
                            break
                    if check:
                        result.append(temp)
    print(result)
else:
    print("Array Input Length Must More Than 2")


