A = input("Please enter the first number:")
B = input("Please enter the second number:")
num1 = 0
num2 = 0
remainder = 0

try:
    A = int(A)
    B = int(B)
except ValueError:
    print("Invalid input. Both values must be integers.")
    exit()

if A == 0 or B == 0:
    print("Invalid input. Both numbers must be non-zero.")
    exit()

if A != 0 and B != 0:
    if A > B:
        num1 = A
        num2 = B
    elif A < B:
        num1 = B
        num2 = A

while num2 != 0:
    remainder = num1 % num2
    num1 = num2
    num2 = remainder

print(f"The Greatest Common Divisor is: {num1}")