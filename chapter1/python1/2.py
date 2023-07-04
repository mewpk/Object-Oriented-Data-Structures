# chapter : 1 - item : 2 - if-elif
# โจทย์: จงเขียนโปรแกรมรับความเร็วลมเฉลี่ยใน 10 นาที และแสดงผลระดับพายุที่เกิดขึ้น จากการจัดแบ่งความเร็วลมดังนี้
#		Speed (km/h)		ระดับพายุ
#			0-51.99			Breeze
#			52.00-55.99		Depression
#			56.00-101.99	        Tropical Storm
#			102.00-208.99	        Typhoon
#			>= 209			Super Typhoon

# โดยแสดงผลตามตัวอย่างการแสดงผล

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