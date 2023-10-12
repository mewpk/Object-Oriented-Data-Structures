# Chapter : 10 - item : 1 - Maze
# หาค่าที่น้อยที่สุดใน Table จากนั้นค่าค่าที่มากที่สุดใน Rows นั้นและหาค่าที่มากที่สุด Column นั้นตามลำดับ 
# โดย Input จะประกอบไปด้วยขนาดกว้างยาวของ Table , ข้อมูลในแต่ละ Cell 

# Ex. 3 3,2 1 3 4 2 4 5 9 2

# Table Size : 3 x 3

# Table : 2 1 3

#             4 2 4

#             5 9 2

# น้อยที่สุด คือ 1 ใน Row 1

# มากที่สุดใน Row 1 คือ 3 ใน Column 3

# มากที่สุดใน Column 3 คือ 4

# Output : 4

def split_list(lst, n):
    # new_lst = []
    # temp = []
    # for i in lst :
    #     temp.append(i)
    #     if len(temp) == n:
    #         new_lst.append(temp)
    #         temp = []
    # return new_lst

    # Use list comprehension to split the list into sublists of size n
    return [lst[i:i + n] for i in range(0, len(lst), n)]


def maze(min_value,lst):
    position = 0
    for index , row in enumerate(lst) :
        if min_value in row :
            min_value = max(row)
            position = index
            break
    col = lst[position].index(min_value)
    for index , row in enumerate(lst) :
        if row[col] > min_value :
            min_value = row[col]
    print(min_value)
        
inp = input("input : ").split(',')
table_size , lst =  tuple(map(int,inp[0].split(" "))) , list(map(int,inp[1].split(" ")))
min_value = min(lst)
lst = split_list(lst,table_size[1])
maze(min_value,lst)

