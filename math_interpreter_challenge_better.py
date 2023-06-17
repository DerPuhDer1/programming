"""
Function to get valid expression from user
Inputs: 
Outputs: 3 values, (int)number 1, (int)number 2, and the (string)operator
"""

def get_valid_expression_input(): 
    while True:
        
        expression = (input("Expression: "))
#Use .split() to get the parts of the expression. Split at the space and check format of expression
        expression_parts = expression.split(" ")
        if len(expression_parts) != 3:
            print("ERROR, please enter expression in (X Y Z) format\n")
            continue
#Get the values from the list
        try: 
            x = int(expression_parts[0])
            z = int(expression_parts[2])
        except ValueError:
            print("ERROR: X and Z must be numbers. (X Y Z)\n")
        
        y = (expression_parts[1])
#test for operator (+, -, *, /)
        if y not in ["+", "-", "*", "X", "/"]:
            print("ERROR: Incorrect operator. Only addition, subtraction, multiplication, division allowed.\n")
            continue
        break
    return x, z, y

"""
Function to evaluate expression
Inputs: (int)x, (int)z, (string)operator
Outputs: (integer)answer
"""
def evaluate_expression(x, z, y):
    if y == '+':
        answer = x+z
    elif y == '-':
        answer = x-z
    elif y == '/':
        answer = x/z
    elif y == 'X':
        answer = x*z
    elif y == '*':
        answer = x*z
    return answer

def main():
    while True:   
#Call get_valid_expresson_input to get the x,y,z values
        x, z, y = get_valid_expression_input()
#Call evaluate_expression to get the answer for the expression
        answer = evaluate_expression(x, z, y)

        print(f"the answer to {x} {y} {z} = {answer:.1f}")
#Ask user if they want to continue
        another_calculation = input("Would you like to evaluate another expression? Press y to continue, any other input to exit: ")
        if another_calculation == "y":
            continue 
        else: 
            break
main()