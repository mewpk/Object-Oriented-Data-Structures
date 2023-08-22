# Chapter : 6 - item : 5 - Segment

# พี่ซันฟงเรียน ToC เยอะไปหน่อยเลยอยากรู้ว่าถ้ามี list ของ string (language) 

# จะสามารถนำ string ใน list มาประกอบเป็นข้อความ text ได้หรือไม่

# ให้เขียนฟังก์ชั่น recursive ที่ชื่อว่า segment และรับ text กับ language คืนค่าเป็น boolean


# def segment(text: str, language: list[str]) -> bool:

#     pass # Write here


# Input

# string ที่มี single quote ครอบไว้อยู่ คั่นด้วย comma

# string อันแรกคือค่าของ text

# ที่เหลือคือ list ของ string (language)

# Output

# บรรทัดที่ 1 ค่าของ text

# บรรทัดที่ 2 ค่าของ language

# บรรทัดที่ 3 ผลลัพธ์ของ segment

 

# รับประกันว่าไม่มีเครื่องหมายคำพูดซ้อนใน string

# รับประกันว่าไม่มี empty string

# แก้ไข parameter ของ segment ได้

# ห้ามใช้ for while รวมถึงตอนรับ input ด้วย

list_lang = []
count = 0
maxcount = 0

def segment(temp_text, language) :

    if len(language) > 0 :
        find = language[language.find("'")+1:language.find("'",language.find("'")+1)]
        list_lang.append(find)
    if len(temp_text) == 0:
        return True
    if len(language) == 0:
        global maxcount
        maxcount = len(list_lang)
        return list_segment(text,list_lang)
    if find in temp_text:
        language = language[language.find("'",language.find("'")+1)+2:]

        return segment(temp_text.replace(find, ''),language )
    else :
        language = language[language.find("'",language.find("'")+1)+2:]
        return segment(temp_text,language )
def list_segment(temp_text, language):
    global count ,maxcount
    # print(temp_text, language)
    if len(temp_text) == 0:
        return True
    
    if count >= maxcount:
        return False
    
    if len(language) == 0:
        count += 1
        return list_segment(text, list_lang[count:]+list_lang[:count])
    if language[0] in temp_text:
        new_temp_text = temp_text.replace(language[0], '')  
        return list_segment(new_temp_text, language[1:])
    
    return list_segment(temp_text, language[1:])

inp = input("Enter list[str]: ")
text = inp[inp.find("'")+1:inp.find("'",inp.find("'")+1)]

lang = inp[inp.find("'",inp.find("'")+1)+3:]
output = segment(text, lang)

print(f"text: str = '{text}'")
print(f"lang: list[str] = {list_lang}")
print(f"segment(text, lang) -> {output}")
