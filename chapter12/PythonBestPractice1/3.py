# Chapter : 12 - item : 3 - count charactors

# จงเขียนโปรแกรมเพื่อรับข้อความ แล้วให้แสดงผล จำนวนตัวอักษรพิมพ์ใหญ่ และ พิมพ์เล็ก และแสดงตัวอักษรที่พบ เรียงตามลำดับตัวอักษร โดยไม่แสดงตัวอักษรซ้ำ และให้แสดงผลตามตัวอย่าง

# หมายเหตุ ให้ระวังตัวอักษรตัวใหญ่ตัวเล็ก ให้ดี


print(" *** String count ***")
text = input("Enter message : ")
upper = 0
lower = 0
list_upper =[]
list_lower =[]
for char in text:
    if char.isupper():
        if char not in list_upper:
            list_upper.append(char)
        upper += 1
    elif char.islower():
        if char not in list_lower:
            list_lower.append(char)
        lower += 1


print(f"No. of Upper case characters : {upper}")
print(f"Unique Upper case characters : {'  '.join(sorted(list_upper))}", end="  \n")
print(f"No. of Lower case Characters : {lower}")
print(f"Unique Lower case characters : {'  '.join(sorted(list_lower))}", end="  ")