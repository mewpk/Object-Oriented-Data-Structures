def weirdSubtract(n,k):

	### Enter Your Code Here ###
    for i in range(k):
        if n % 10 == 0:
            n /= 10
        else :
            n -= 1
    
    return round(n)

n,s = input("Enter num and sub : ").split()

print(weirdSubtract(int(n),int(s)))