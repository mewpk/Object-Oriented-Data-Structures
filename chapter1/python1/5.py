# Chapter : 1 - item : 5 - Countdown มหาสนุก

# อยากให้นักศึกษาช่วยหาลำดับการ Countdown จาก Input ที่รับเข้ามา โดยลำดับการ Countdown จะเป็นเลขเรียงลำดับ เช่น 2->1 , 3->2->1 โดยจะสิ้นสุดด้วย 1 เสมอ
#     โดยผลลัพธ์ให้แสดง List ของ จำนวนลำดับที่เจอ และ แต่ละลำดับเป็นอย่างไร




print("*** Fun with countdown ***")
number  = list(map(int,input("Enter List : ").split(" ")))

list_all_countdown =  []
list_countdown = []
answer =  []

for i in range(len(number)-1 , 0 , -1):
    if number[i] == 1:
        list_countdown.append(number[i])
    if number[i] == number[i-1] - 1 and list_countdown != [] and number[i-1] >= 1:
        list_countdown.append(number[i-1])
    else :
        if list_countdown != [] :
            list_all_countdown.append(list(reversed(list_countdown) ))
        list_countdown = []

if list_countdown != [] :
        list_all_countdown.append(list(reversed(list_countdown) ))

if number[0] == 1:
    list_all_countdown.append([1])
list_all_countdown.reverse()

answer.insert(0 , len(list_all_countdown))
answer.append(list_all_countdown)

print(answer)