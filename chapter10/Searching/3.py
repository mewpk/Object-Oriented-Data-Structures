# หาค่า Simple-square-root ของจำนวนเต็มบวก x  โดย simple-sqrt 
# คือ จำนวนเต็มที่เมื่อยกกำลังแล้ว จะมีค่าใกล้เคียงหรือเท่ากับ x มากที่สุด

# ห้ามใช้ฟังก์ชันช่วยในการหาค่า เช่น sqrt(x), pow(x,0.5) เป็นต้น ให้ใช้ binary-search 

# Example 1:
# Input:
# Enter input: 4

# Output:
# Simple sqrt: 2

# -----------------------------
# Example 2:
# Input:
# Enter input: 8

# Output:
# Simple sqrt: 2

# อธิบาย Example 2:
# sqrt(8) = 2.82842...
# ดังนั้น ค่าที่ยกกำลังแล้วและเป็นจำนวนเต็ม ที่ใกล้กับ 8 คือ 2

def simple_sqrt(x, epsilon=1e-6):
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    if x == 0:
        return 0
    left = 0
    right = max(1, x)
    while right - left > epsilon:
        mid = (left + right) / 2
        mid_squared = mid * mid
        
        if mid_squared == x:
            return mid
        
        if mid_squared < x:
            left = mid
        else:
            right = mid
    print((left + right)/2)
    return (left + right) / 2

x = int(input("simple sqrt: "))
result = simple_sqrt(x)
print(int(result))
