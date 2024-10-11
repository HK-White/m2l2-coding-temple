# Task 1: Code Correction

number = input("Enter a number: ")
#error3
if int(number) > 0:
    print("The number is positive.")
elif int(number) == 0:             #error2
    print("The number is zero.")
else:
    print("The number is negative.")                  #Error 1
#Error1 was the fact that a < 0 was placed by
#else which is the opposite of the if statement.
#Error2 was the fact that = was used instead of ==.
#Error3 was the fact that the number was not converted to an integer.