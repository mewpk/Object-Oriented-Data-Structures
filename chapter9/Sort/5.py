
# Chapter : 9 - item : 5 - คู่ตัวเลขเด่น
#  ส่งมาแล้ว 0 ครั้ง
# ให้ชุดของคู่อันดับจํานวนเต็มบวกมา n ชุด คือ (a1, b1),(a2,b2),...,( an, bb)

# โดยที่ ai≠aj ถ้า i ≠ jและ bk ≠ bl ถ้า k ≠ l  เราเรียกคู่อันดับ 2 คู่ (ai ,bi )และ (aj ,bj ) 
# ว่าคู่ตัวเลขเด่นก็ต่อเมื่อ  ai > aj และ bi < bj  พี่ซันฟงอยากเขียนโปรแกรมที่มีประสิทธิภาพใน
# การหาค่าผลรวมของ ai + aj ทั้งหมด เมื่อ คู่ ( ai,bi ) และ ( aj, bj)  เป็นคู่ตัวเลขเด่น



# *** บังคับให้มี merge sort ***

# 2 1 7 6 9 3 18 4 3 2 5 5
                               
# (2,1) (7,6) (9,3) (18,4) (3,2) (5,5)

# (18,4) (9,3) (7,6) (5,5) (3,2) (2,1)

# (18,4) (7,6)
# (18,4) (5,5)
# (9,3) (7,6)
# (9,3) (5,5)
def is_special_pair(pair1, pair2):
    return pair1[0] > pair2[0] and pair1[1] < pair2[1]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i][0] >= right[j][0]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged

def main():
    input_values = [int(x) for x in input("input : ").split()]
    pairs = [(input_values[i], input_values[i+1]) for i in range(0, len(input_values), 2)]
    
    sorted_pairs = merge_sort(pairs)
    
    total_sum = 0
    for i in range(len(sorted_pairs) - 1):
        for j in range(i + 1, len(sorted_pairs)):
            if is_special_pair(sorted_pairs[i], sorted_pairs[j]):
                total_sum += sorted_pairs[i][0] + sorted_pairs[j][0]
    
    print(f"ans = {total_sum}")

if __name__ == "__main__":
    main()
