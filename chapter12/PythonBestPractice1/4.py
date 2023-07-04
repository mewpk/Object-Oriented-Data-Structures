print("*** String Rotation ***")
text1 , text2 =  input("Enter 2 strings : ").split(" ")
text1 = list(text1)
text2 = list(text2)
temp1 , temp2 = text1[:] ,text2[:]
# print(text1 , text2)
i = 0
while True :
    i += 1
    temp1.insert(0,temp1.pop(len(temp1)-1)) 
    temp1.insert(0,temp1.pop(len(temp1)-1))
    temp2.insert(len(temp1)+1,(temp2.pop(0)))
    temp2.insert(len(temp1)+1,(temp2.pop(0)))
    temp2.insert(len(temp1)+1,(temp2.pop(0)))
    
    
    if (temp1 == text1)  and (temp2 == text2):
        print(f"{i} {''.join(temp1)} {''.join(temp2)}")
        print(f"Total of  {i} rounds.")
        break
    
    if i <= 5 :
        print(f"{i} {''.join(temp1)} {''.join(temp2)}")
    if i == 6 :
        print(" . . . . .")