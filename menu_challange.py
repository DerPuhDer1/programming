#make the dictionary 
menu = {"Baja Taco": 4.00, "Burrito": 7.50, "Bowl": 8.50, "Nachos": 11.00, "Quesadilla": 8.50, "Super Burrito": 8.50, "Super Quesadilla": 9.50, "Taco": 3.00, "Tortilla Salad": 8.00}
#ask the user what item they want, and display the total, if they put in "end" break
total = 0
while True: 
    user_food = input("Item: ")
    if user_food.lower() == "end":
        break
    if user_food not in menu.keys() :
        continue

    total = menu[user_food] + total
    print(f"${total:.2f}")