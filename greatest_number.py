number1 = int(input("Your first number please: "))
number2 = int(input("Now your second number: "))
number3 = int(input("Finally your third number: "))

if (number1 >= number2) and (number1 >= number3):
   largest = number1
elif (number2 >= number1) and (number2 >= number3):
   largest = number2
else:
   largest = number3

print("The largest number is", largest )

if (number1 <= number2) and (number1 <= number3):
   smallest = number1
elif (number2 >= number1) and (number2 <= number3):
   smallest = number2
else:
   smallest = number3

print("The smallest number is", smallest)

# Figured this out with the official python documents