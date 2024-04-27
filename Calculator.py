flag = "True"

while flag == "True":
    print("Wanna calculate some numbers? Type 'N' at any time to stop:\n")
    
    number1 = float(input("Type your first number: \n"))
    
    number2 = float(input("Type your second number: \n"))

    operator = str(input("Enter your operator(+,-,*,/,//,%,**): \n"))

    solution = "Thanks for playing"
    if operator == "N":
        flag = "false"
    if operator == "+":
        solution = number1 + number2
    elif operator == "-":
        solution = number1 - number2
    elif operator == "*":
        solution = number1 * number2
    elif operator == "/":
        solution = number1 / number2
    elif operator == "//":
        solution = number1 // number2
    elif operator == "%":
        solution = number1 % number2
    elif operator == "**":
        solution = number1 ** number2
    
    print(f"Solution: {solution}")
