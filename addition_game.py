#import random +
#Prompt for level +
#Prompt for question amount +
#Define the function to generate questions +
#Prompt the user to give answer +
#check rightness of answer +
#If answer is wrong, prompt again (max of three prompts) for loop, if they are right break if not continue +
#print how many they got right
#Prompt user to see if they want to play again


import random 

def generate_number(x,y):
    number1 = random.randint(x,y)
    return number1

while True:
    level = int(input("Enter level (1, 2, or 3): "))
    if level in [1, 2, 3,]:
        break
    else:
        print("ERROR: Invalid input")
        continue

while True:
    number_of_questions = int(input("Enter the amount of questions you want (1-10): "))
    if number_of_questions in [1,2,3,4,5,6,7,8,9,10]:
        break
    else: 
        continue

def get_answer():
    b = 1
    for a in range(3):
        while True:
            try:
                user_answer = int(input(f"{number1} + {number2} = "))
                break
            except(ValueError):
                print("ERROR: Please enter a valid positive number")
                continue
        if user_answer == answer:
            wrong_answer = 0
            print("Correct!")
            break
        elif b<= 2:
            print("Incorrect!!")
            b = b + 1
            continue
        elif b == 3:
            print("Incorrect \n")
            print(f"Correct answer: {answer}")
            wrong_answer = 1
            break
    return wrong_answer


if level == 1:
    x = 0
    y = 9
elif level == 2:
    x = 10
    y = 99
elif level == 3:
    x = 100
    y = 999

for z in range(number_of_questions):
    b = 1
    number1 = generate_number(x,y)
    number2 = generate_number(x,y)
    answer = number1 + number2
    get_answer()

def main():
    amount_wrong = 0
    for z in range(number_of_questions):
        amount_wrong = get_answer()
        wrong_answer = wrong_answer + amount_wrong
    amount_right = number_of_questions - wrong_answer
    percent_right = amount_right / number_of_questions * 100
    print(f"You got {amount_right} out of {number_of_questions} questions correct. {percent_right:.2f}")

main()
    
