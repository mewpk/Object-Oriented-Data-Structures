print("*** Mod Position ***")

def mod_position(arr, s):
    temp = []

    for i in range(1,len(arr)+1):
        if i % int(s) == 0:
            temp.append(arr[i-1])
    return temp


arr,s = input("Enter Input : ").split(",")
print(mod_position(arr, s))