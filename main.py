""" Convert_to_a_number"""
first_num = input("Enter the number: ")
second_num = input("Enter the number: ")

try:
    num1 = float(first_num)
    num2 = float(second_num)

    print(num1, num2)

except ValueError:
    print("The value entered is not a number")
