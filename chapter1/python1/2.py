print(" *** Wind classification ***")
number = float(input("Enter wind speed (km/h) : "))
if number >= 209: # [209 , inf)
    print("Wind classification is Super Typhoon.")
elif number >= 102.0 :
    print("Wind classification is Typhoon.")
elif number >= 56.0 :
    print("Wind classification is Tropical Storm.")
elif number >= 0 :
    print("Wind classification is Breeze.")