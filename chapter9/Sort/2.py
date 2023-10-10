# Chapter : 9 - item : 2 - เรียงลำดับโดยไม่สนจำนวนเต็มลบ

# ให้เรียงลำดับ input จากน้อยไปมากของจำนวนเต็มบวกและศูนย์ โดยถ้าหากเป็นจำนวนเต็มลบไม่ต้องยุ่งกับมัน

# ****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง


inp = list(map(int,input("Enter Input : ").split(" ")))

def sort(inp):
    dict = {}
    temp = inp.copy()
    for index ,  value  in enumerate(temp):
        if value < 0 :
            dict.update({index : value})
            inp.remove(value)
    while True :
        check = True
        for i in range(len(inp)-1):
            if inp[i] > inp[i+1]:
                inp[i], inp[i+1] = inp[i+1], inp[i]
                check = False
        if check:
            break
    for key , value in dict.items():
        inp.insert(key,value)

    return inp

print(" ".join(list(map(str,sort(inp)))))