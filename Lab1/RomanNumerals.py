Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
#Decimal to Roman Numerals
def int2roman(number):
 numeralOrder = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
 numeralLetters = {
 1000 : "M", 900 : "CM", 500 : "D", 400 : "CD",
 100 : "C", 90 : "XC", 50 : "L", 40 : "XL",
 10 : "X", 9 : "IX", 5 : "V", 4 : "IV",
 1 : "I" }
 result = ""
 if number < 1 or number > 4999:
 raise ValueError
 for value in numeralOrder:
 while number >= value:
 result += numeralLetters[value]
 number -= value
 return result
try:
 print(int2roman(int(input("Enter an integer (1 to 4999): "))))
except ValueError:
 print("Try again")