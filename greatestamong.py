# WAP to find the greatest number among three numbers

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Assume that greatest number is number1
greatest_number = number1

if number1 > greatest_number:
    greatest_number = number1

if number2 > greatest_number:
    greatest_number = number2

if number3 > greatest_number:
    greatest_number = number3

print("Greatest number = ", greatest_number)
1