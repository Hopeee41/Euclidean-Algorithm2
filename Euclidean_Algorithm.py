class GCD:
    def __init__(self,A,B):
        # Initialise variables
        self.A = A
        self.B = B
        self.num1 = 0
        self.num2 = 0
        self.remainder = 0
        self.result = 0
        self.list1 = []

    def valid(self):
        # Check if it is can convert into integer. If yes, continue; If no, print.
        try:
            self.A = int(self.A)
            self.B = int(self.B)
        except ValueError:
            print("Invalid input. Both values must be integers.")
            exit()

        # Check if A or B is zero. If no, continue; If yes, print.
        if self.A == 0 or self.B == 0:
            print("Invalid input. Both numbers must be non-zero.")
            exit()

    # Set the bigger number as num1; smaller number as num2.
    def assign_numbers(self):
        if self.A > self.B:
            self.num1 = self.A
            self.num2 = self.B
        elif self.A < self.B:
            self.num1 = self.B
            self.num2 = self.A

    # When num2 is zero, loop ends. Set the greatest common divisor as num1
    def result(self):
        while self.num2 != 0:
            self.result = self.num1 // self.num2
            self.remainder = self.num1 % self.num2
            print(f"{self.num1} = {self.num2} * {self.result} + {self.remainder}")
            self.list1.append(self.num2)
            self.list1.append(self.remainder)
            print(self.list1)
            self.num1 = self.num2
            self.num2 = self.remainder
            self.list1 = []
        return self.num1

#Input two variables
A = input("Please enter the first number: ")
B = input("Please enter the second number: ")

# Create a GCD object and calculate the result
gcd_calculator = GCD(A,B)
gcd_calculator.valid()
gcd_calculator.assign_numbers()
gcd = gcd_calculator.result()

print(f"The Greatest Common Divisor is: {gcd}")


