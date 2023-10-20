def sqrt_v2(inp):
    max_value = 1e-6
    middel_value = inp/2
    left_value = 0
    right_value = inp
    while right_value - left_value > max_value :
        if middel_value**2 > inp:
            middel_value ,right_value = (left_value + middel_value)/2 , middel_value
        elif middel_value**2 < inp:
            middel_value , left_value = (right_value + middel_value)/2 , middel_value
        else :
            return middel_value
    return middel_value



inp = input("Enter Input : ")
print(sqrt_v2(int(inp)))