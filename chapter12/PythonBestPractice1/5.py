class MyInt:
    def __init__(self, number):
        self.number = number
        self.roman_dict = {"M": 1000,
                           "CM": 900,
                           "D": 500,
                           "CD": 400,
                           "C": 100,
                           "XC": 90,
                           "L": 50,
                           "XL": 40,
                           "X": 10,
                           "IX": 9,
                           "V": 5,
                           "IV": 4,
                           "I": 1
                           }

    def toRoman(self):
        temp_number = self.number
        roman = ""
        while temp_number > 0 :
            for key in self.roman_dict:
                if temp_number >= self.roman_dict[key]:
                    temp_number -= self.roman_dict[key]
                    roman += key
                    break
            else:
                break
        return f"{self.number} convert to Roman : {roman}"

    def __add__(self, other):
        new_number = self.number + other.number
        new_number += new_number/2
        return MyInt(int(new_number))

    def __str__(self) -> str:
        return f"{number1} + {number2} = {str(self.number)}"

print(" *** class MyInt ***")
number1, number2 = list(map(int,input("Enter 2 number : ").split(" ")))

a = MyInt(number1)

b = MyInt(number2)

print(a.toRoman())

print(b.toRoman())

print(a+b)
