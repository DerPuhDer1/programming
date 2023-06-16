#Ask user for input
while True:
        while True:  
            expression = (input("Expression: "))
        #Use .split() to get the parts of the expression. Split at the space and check format of expression
            expression_parts = expression.split(" ")
            if len(expression_parts) != 3:
                print("ERROR, please enter expression in (X Y Z) format\n")
                continue

    #Get the values from the list
            x = int(expression_parts[0])
            y = expression_parts[1]
            z = int(expression_parts[2])

            #test for operator (+, -, *, /)
            if y not in ["+", "-", "*", "X", "/"]:
                print("ERROR: Incorrect operator. Only addition, subtraction, multiplication, division allowed.\n")
                continue
            break
    #Determine the operation. Using if/elif/else statement and print the answer formatted using one decimal place
        if expression_parts[1] == '+':
            answer = x+z
            print(f"the answer to {x} + {z} = {answer:.1f}")
        elif expression_parts[1] == '-':
            answer = x-z
            print(f"the answer to {x} - {z} = {answer:.1f}")
        elif expression_parts[1] == '/':
            answer = x/z
            print(f"the answer to {x} / {z} = {answer:.1f}")
        elif expression_parts[1] == 'X':
            answer = x*z
            print(f"the answer to {x} X {z} = {answer:.1f}")
        elif expression_parts[1] == '*':
            answer = x*z
            print(f"the answer to {x} * {z} = {answer:.1f}")

    #Ask user if they want to continue
        another_calculation = input("Would you like to evaluate another expression? Press y to continue, any other input to exit: ")
        if another_calculation == "y":
            continue 
        else: 
            break