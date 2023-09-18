# Chapter : 5 - item : 5 - Radix Sort (มากไปน้อย)
# ให้น้องๆใช้ Linked List (เขียนเป็น class)  ในการทำ Radix Sort  (มีอยู่ในสไลด์เรียน 2 หน้าสุดท้าย)  ในรูปแบบมากไปน้อย

# โดยผลลัพธ์ให้ออกมาเป็นการทำ Radix Sort แบบจำนวนรอบน้อยที่สุด และแสดงผลในแต่ละรอบว่าได้ผลลัพธ์เป็นอย่างไร  3 บรรทัดสุดท้ายจะเป็น ( จำนวนรอบที่น้อยที่สุด , Data ก่อนทำ Radix Sort และ Data หลังทำ Radix Sort )

# Enter Input : 64 8 216 512 27 729 0 1 343 125
# ------------------------------------------------------------
# Round : 1
# 0 : 0 
# 1 : 1 
# 2 : 512 
# 3 : 343 
# 4 : 64 
# 5 : 125 
# 6 : 216 
# 7 : 27 
# 8 : 8 
# 9 : 729 
# ------------------------------------------------------------
# Round : 2
# 0 : 8 1 0 
# 1 : 216 512 
# 2 : 729 27 125 
# 3 : 
# 4 : 343 
# 5 : 
# 6 : 64 
# 7 : 
# 8 : 
# 9 : 
# ------------------------------------------------------------
# Round : 3
# 0 : 64 27 8 1 0 
# 1 : 125 
# 2 : 216 
# 3 : 343 
# 4 : 
# 5 : 512 
# 6 : 
# 7 : 729 
# 8 : 
# 9 : 
# ------------------------------------------------------------
# 3 Time(s)
# Before Radix Sort : 64 -> 8 -> 216 -> 512 -> 27 -> 729 -> 0 -> 1 -> 343 -> 125
# After  Radix Sort : 729 -> 512 -> 343 -> 216 -> 125 -> 64 -> 27 -> 8 -> 1 -> 0

class LinkedList:
    def __init__(self) -> None:
        self.head = self.tail = None
    def append(self,data) :
        if not self.head :
            self.head = self.tail = data
        else :
            self.tail.next = data
            self.tail = data 
    def __str__(self) -> str:
        cur = self.head
        temp = []
        while cur :
            temp.append(f"{cur.data}")
            cur = cur.next
        return ' -> '.join(temp)


class Node :
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

prev_data = LinkedList()
list_number = input("Enter Input : ").split(" ")

def radix_sort(arr):
    maxnumber = max(arr)
    maxdigit = len(str(maxnumber))

    bucket =  [[] for _ in range(10)]

    for digit in range(1) :
        for number in arr :
            n = Node(number)
            position = (number // 10 ** digit) % 10
            print(position)
            bucket[position].append(number)
    print(bucket)


for data in list_number :
    n = Node(data)
    prev_data.append(n)
print(prev_data)
radix_sort(list(map(int,list_number)))



# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node

# def print_buckets(buckets):
#     for i, bucket in enumerate(buckets):
#         print(f'{i} :', end=' ')
#         current = bucket.head
#         while current:
#             print(current.data, end=' ')
#             current = current.next
#         print()

# def radix_sort(arr):
#     # Find the maximum number to know the number of digits
#     max_num = max(arr)
#     num_digits = len(str(max_num))

#     # Create a list of linked lists (buckets) for each digit position (0-9)
#     buckets = [LinkedList() for _ in range(10)]

#     for digit_position in range(num_digits):
#         print("-" * 60)
#         print(f"Round : {digit_position + 1}")
        
#         # Distribute elements into buckets based on the current digit
#         for num in arr:
#             digit = (num // 10 ** digit_position) % 10
#             buckets[digit].append(num)
        
#         # Print the buckets for this round
#         print_buckets(buckets)

#         # Collect elements from buckets in order and update the original array
#         arr = []
#         for bucket in buckets:
#             current = bucket.head
#             while current:
#                 arr.append(current.data)
#                 current = current.next

#         # Clear the buckets for the next iteration
#         buckets = [LinkedList() for _ in range(10)]

#     print("-" * 60)
#     print(f"{num_digits} Time(s)")
#     print(f"Before Radix Sort : {' -> '.join(map(str, arr))}")
#     print(f"After  Radix Sort : {' -> '.join(map(str, arr))}")

# # Example usage
# arr = [64, 8, 216, 512, 27, 729, 0, 1, 343, 125]
# radix_sort(arr)
