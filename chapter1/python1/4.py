def odd_list(al):
    # เติมส่วนของคำสั่ง
    for i in al :
        if i % 2 != 0 :
            yield i


print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
opls = list(odd_list(ls))
print("Input list : ", ls, "\nOutput list : ", opls)