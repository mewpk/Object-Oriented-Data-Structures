# Chapter : 9 - item : 4 - Sort by alphabet
# ให้เรียงลำดับ input ที่รับเข้ามาจากน้อยไปมาก โดยเรียงลำดับจากตัวอักษรที่มีอยู่
# ในแต่ละ string โดยตัวอักษรจะมีแค่ a - z เท่านั้น และในแต่ละ string จะมี alphabet เพียงแค่ 1 ตัวเท่านั้น

# ****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง

inp = input("Enter Input : ").split(" ")

def sort(lst):
    dict = {}
    lst_key = []
    for string in lst :
        for char in string :
            if char.isalpha():
                dict.update({char : string})
                count = 0
                for key in lst_key :
                    if char < key :
                        break
                    count += 1
                lst_key.insert(count,char)
                break
    # print(lst_key)
    # print(dict)
    temp = []
    for key in lst_key :
        temp.append(dict[key])
    print(" ".join(temp))
sort(inp)