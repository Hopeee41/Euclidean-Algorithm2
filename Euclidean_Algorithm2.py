A = input("Please enter the first number:")
B = input("Please enter the second number:")
num1 = 0
num2 = 0
remainder = 0
result = 0
list1 =[]

# Check if it is can convert into integer. If yes, continue; If no, print.
try:
    A = int(A)
    B = int(B)
except ValueError:
    print("Invalid input. Both values must be integers.")
    exit()

# Check if A or B is zero. If no, continue; If yes, print.
if A == 0 or B == 0:
    print("Invalid input. Both numbers must be non-zero.")
    exit()

# Set the bigger number as num1; smaller number as num2.
if A != 0 and B != 0:
    if A > B:
        num1 = A
        num2 = B
    elif A < B:
        num1 = B
        num2 = A

# When num2 is zero, loop ends. Set the greatest common divisor as num1
while num2 != 0:
    result = num1 // num2
    remainder = num1 % num2
    print(f"{num1} = {num2} * {result} + {remainder}")
    list1.append(num2)
    list1.append(remainder)
    print(list1)
    num1 = num2
    num2 = remainder
    list1 = []

print(f"The Greatest Common Divisor is: {num1}")
