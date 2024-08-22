# Get three numbers from the user
num1 = int (input("Enter the first number: "))
num2 = int (input("Enter the second number: "))
num3 = int (input("Enter the third number: "))

# Identify the largest number
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("The Largest number is",(largest),"!")

# Identify the smallest number
if num1 <= num2 and num1 <= num3:
    smallest = num1
elif num2 <= num1 and num2 <= num3:
    smallest = num2
else:
    smallest = num3

print("The Smallest number is",(smallest),"!")
