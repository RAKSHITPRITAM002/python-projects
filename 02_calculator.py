FirstNumber=float(input("Enter first number:"))
SecondNumber=float(input("Enter Second Number:",))

print("Choose any operator:")
print("+ for addition")
print("- for subtraction")
print("* for multiplication")
print("/ for divison")


operator = input("Type the operator first: ",)

if operator == "+":
    print("The result is", FirstNumber + SecondNumber)
elif operator == "-":
    print("The result is", FirstNumber - SecondNumber)
elif operator == "*":
    print("The result is", FirstNumber * SecondNumber)
elif operator == "/":
    if SecondNumber != 0:
        print("The result is", FirstNumber / SecondNumber)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operator")