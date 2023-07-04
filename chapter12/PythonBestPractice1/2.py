print(" *** Divisible number ***")
number = int(input("Enter a positive number : "))
if number <= 0:
    print(f"{number} is OUT of range !!!")
else : 
    list = []
    for i in range(1, number + 1):
        if number % i == 0:
            list.append(i)
    print(f"Output ==> {' '.join(map(str,list))}")
    print(f"Total ==> {len(list)}")
