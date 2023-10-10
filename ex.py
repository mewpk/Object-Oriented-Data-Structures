list1 = [2,3,13,15,4,1,12,18]
print(sum(list1))
list1.sort(reverse=True)
print(list1[:int((len(list1))/2)])
print(list1[int((len(list1))/2):][::-1])
temp1 = list1[:int((len(list1))/2)]
temp2 = list1[int((len(list1))/2):][::-1]

count = 0
for i in range(1,len(temp1)*2,2):
    temp1.insert(i,temp2[count])
    count += 1
print(temp1)

2 1 7 6 9 3 18 4 3 2 5 5
                               
(2,1) (7,6) (9,3) (18,4) (3,2) (5,5)

(18,4) (9,3) (7,6) (5,5) (3,2) (2,1)

(18,4) (7,6)
(18,4) (5,5)
(9,3) (7,6)
(9,3) (5,5)