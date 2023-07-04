# Chapter : 1 - item : 3 - Fun with permute
# เขียนโปรแกรม Python เพื่อสร้างวิธีเรียงสับเปลี่ยนที่เป็นไปได้ทั้งหมดจากชุดตัวเลขที่กำหนด


def permute(lst):
    list_number = []
    lst.reverse()
    list_number.append(lst.copy())
    for round in range(1, len(lst) - 1):
        copy_lst = lst.copy()

        for n in range(len(lst) - 1):
            if n != 0 :
                copy_lst[n], copy_lst[n + 1] = copy_lst[n + 1], copy_lst[n]
                list_number.append(copy_lst.copy())
                
            new_lst = copy_lst.copy()
            for m in range(len(new_lst) - 1):
                new_lst[m], new_lst[m + 1] = new_lst[m + 1], new_lst[m]
                list_number.append(new_lst.copy())
                
        if round < len(lst) - 2:
            lst[round + 1], lst[round + 2] = lst[round + 2], lst[round + 1]
            list_number.append(lst.copy())

    return list_number

print("*** Fun with permute ***")
number = list(map(int, input("input : ").split(",")))
print(f"Original Cofllection:  {number}")
print(f'Collection of distinct numbers:\n {permute(number)}')
