# Chapter : 5 - item : 3 - trains
# สถานณีรถไฟแห่งหนึ่งมีจำนวนโบกี้เยอะมาก ทำให้เจ้าหน้าที่งุนงงและสับสนจึงขอให้คุณที่เป็นสุดยอดโปรแกรมเมอร์ 
# มาเขียนโปรแกรมเพื่อจัดการโบกี้ต่างๆให้ดูง่ายมากยิ่งขึ้น



# โดย n คือ จำนวนโบกี้รถไฟทั้งหมด และ string ต่อจากนั้น คือ อันดับการต่อกันของโบกี้ต่างๆจะถูกคั่นด้วย "," 
# โดย u-v คือ โบกี้ u จะถูกต่อด้วย v 



# งานของคุณ คือ หาจำนวนรถไฟและโบกี้ที่เหลือทั้งหมด และแสดงขบวนรถไฟทั้งหมดในรูปแบบของ 
# link-list โดยให้แสดงเรียงตามหัวขบวนที่มีเลขน้อยสุดก่อน



# Example 1:

# Input:

# Enter input: 6 4-5,5-6,6-1,1-2,2-3



# Output:

# 1: 4->5->6->1->2->3

# Number of train(s): 1



# อธิบาย:

# มีจำนวน 6 โบกี้ โดยโบกี้ที่ 4 จะถูกต่อด้วยโบกี้ที่ 5, โบกี้ที่ 5 จะถูกต่อด้วยโบกี้ที่ 6, โบกี้ที่ 6 จะถูกต่อด้วยโบกี้ที่ 1,

# โบกี้ที่ 1 จะถูกต่อด้วยโบกี้ที่ 2 และโบกี้ที่ 2 จะถูกต่อด้วยโบกี้ที่ 3 ทำให้มีจำนวนรถไฟทั้งหมด 1 ขบวน





# Example 2:

# Input:

# Enter input: 6 4-5,5-6,1-2,2-3



# Output:

# 1: 1->2->3

# 2: 4->5->6

# Number of train(s): 2



# อธิบาย:

# มีจำนวน 6 โบกี้ โดยโบกี้ที่ 1 จะถูกต่อด้วยโบกี้ที่ 2, โบกี้ที่ 2 จะถูกต่อด้วยโบกี้ที่ 3 นับเป็น 1 ขบวน และโบกี้ที่ 4 จะถูกต่อด้วยโบกี้ที่ 5,

# โบกี้ที่ 5 จะถูกต่อด้วยโบกี้ที่ 6 นับเป็นอีก 1 ขบวน ทำให้มีจำนวนรถไฟทั้งหมด 2 ขบวน





# Example 3:

# Input:

# Enter input: 5 1-2,3-1 



# Output:

# 1: 3->1->2

# 2: 4

# 3: 5

# Number of train(s): 3



# อธิบาย:

# มีจำนวน 5 โบกี้ 

# โดยโบกี้ที่ 1 จะถูกต่อด้วยโบกี้ที่ 2: 1->2

# โบกี้ที่ 3 จะถูกต่อด้วยโบกี้ที่ 1 อีกที: 3->1->2 นับเป็น 1 ขบวน

# ส่วนโบกี้ที่ 4 และโบกี้ที่ 5 ไม่มีการต่อ นับเป็น 2 ขบวน

# ทำให้มีจำนวนรถไฟทั้งหมด 3 ขบวน

class Node :
    def __init__(self , data , next=None) :
        self.value = data
        if next :
            self.next = next
        else :
            self.next = None
    def __str__(self) -> str :
        return f"{self.value}"
class LinkedList :
    def __init__(self , head = None):
        if head :
            self.head = head
            
        else :
            self.head = None
            

    def __str__(self) -> str:
        cur = self.head
        s = []
        while cur :
            s.append(cur.value)
            cur = cur.next
        return "->".join(s)
    def isEmpty(self) :
        return self.head == None
    
    def append(self,data) :
        if not self.head :
            self.head = data
    def size(self) :
        cur = self.head
        count = 0
        while cur :
            count += 1
            cur = cur.next
        return count




total,bokies  = input("Enter input: ").split(" ")
bokies = bokies.split(",")
# print(total,bokies)
l1 = LinkedList()
list_linkedlist = [l1]
found = False
for boky in bokies :
    data,nextdata = boky.split("-")
    n1 = Node(data)
    n2 = Node(nextdata)
    n1.next = n2
    for linked in list_linkedlist :
        if not found :
            if not linked.head :
                linked.append(n1)
                found = True
            else :
                cur = linked.head 
                while cur :
                    if cur.value == n2.value and cur == linked.head:
                        linked.head = n1
                        n1.next = cur
                        found = True
                        break
                    elif cur.value == n2.value :
                        n1.next = cur
                        found = True
                        break
                    elif cur.value == n1.value :
                        cur.next = n2
                        found = True
                        break
                    cur = cur.next
    if found == True :
        found = False
    else :
        l2 = LinkedList()
        l2.append(n1)
        list_linkedlist.append(l2)
list_total = list(map(str,range(1,int(total)+1)))
for linked in list_linkedlist :
    cur = linked.head
    while cur :
        try :
            list_total.remove(cur.value)
        except :
            break
        cur = cur.next
for str in list_total :
    n = Node(str)
    temp = LinkedList()
    temp.append(n)
    # print(temp)
    list_linkedlist.append(temp)

def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if int(arr[j].head.value) > int(arr[j + 1].head.value):
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return
bubbleSort(list_linkedlist)

list_temp = list_linkedlist[:]

for linked1 in list_temp:
    if linked1 :
        if linked1.size() > 1 :
            cur1 = linked1.head
            for linked2 in list_temp :
                if linked2 and linked1 :
                    if linked2.size() > 1 and linked2 is not linked1 :
                        cur2 = linked2.head 
                        while cur2 :
                            if cur2.value == cur1.value :
                                cur2.next = cur1.next
                                if linked1 in list_linkedlist :
                                    list_linkedlist.remove(linked1)
                                break
                            cur2 = cur2.next
i = 0
for linked in list_linkedlist :
    i += 1
    print(f"{i}: {linked}")
print(f"Number of train(s): {i}")