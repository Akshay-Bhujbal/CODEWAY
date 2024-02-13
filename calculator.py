
def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def devide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return("Error. Division by zero is not allowed")

print("Simple Calculator")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Devision")

while True:
    choice = input("Enter the operation number (1/2/3/4): ")

    if choice in ("1","2","3","4"):
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))

        if choice == "1":
            print("Addition: ", add(n1, n2))

        elif choice == "2":
            print("Substaction: ", substract(n1, n2))

        elif choice == "3":
            print("Multiplication: ", multiply(n1, n2))

        elif choice == "4":
            print("Devision: ", devide(n1, n2))
    else:
        print("Invalid Input")

    next_calculation = input("Do you want to perform another calculation? (y/n): ")
    if next_calculation != "y":
        break