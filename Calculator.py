first = input("Enter the first number : ")
operator = input("select  the operator i.e (+,-,*,/,%) : ")
second = input("Enter the second number :")

first = float(first)
second = float(second)

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)
else :
    print("Invalid Operator Selected")