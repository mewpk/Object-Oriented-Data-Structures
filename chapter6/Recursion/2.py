# Chapter : 6 - item : 2 - Reverse Sort List

# จงเขียนฟังก์ชั่นสำหรับการเรียงค่าใน List ของจำนวนเต็มโดยจะเรียงค่าจากมากไปน้อย

# ****ห้ามใช้ for/while และฟังก์ชั่นอื่นๆในการวนลูป ให้ใช้ recursion ในการเขียนเท่านั้น****

# list_number = []
list_reverse = []

def find_max(list):
    # print(list)
    list = list.copy()
    if len(list) == 1:
        return list[0]
    if list[0] > list[1]:
        list.remove(list[1])
        return find_max(list)
    return find_max(list[1:])

def reverse_sort_list(lst):
    if len(lst) < 1:
        return lst
    
    max_number = find_max(lst)  
    list_reverse.append(max_number)  
    
    lst.remove(max_number)  
    
    return reverse_sort_list(lst)  


# def string_to_list_integer(text):
#     if len(text) <= 0:
#         return
#     elif text[0] != "," :
#         list_number.append(int(text[0]))
#     string_to_list_integer(text[1:])



inp = list(map(int,input("Enter your List : ").split(",")))
# inp = string_to_list_integer(input("Enter your List : "))


reverse_sort_list(inp)

print(f"List after Sorted : {list_reverse}")