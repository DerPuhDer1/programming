#Function to load menu items and cost into a get_menu_dictionary
#Input: none 
#Output: Dictionary of menu items and the cost
def get_menu_dictionary():
    #open the file
    data_file = open("file.txt", "r")

    #Create an empty dictionary
    menu_item = {}

    #Loop through data in file
    for line_of_data in data_file:
        #Split line of data at the ", "
        keys_values = line_of_data.split(", ")
        #Create an entry to the dictionary. Remember to convert price to float
        menu_item[keys_values[0]] = float(keys_values[1])

    #Close file
    data_file.close()

    return menu_item


def main():

    menu_items = get_menu_dictionary()
    
    total = 0
    while True:
        #prompt the user of a menu item
        item = input("Item: ")

        #determine if we need to end the program
        if item.lower() == "end":
            break
        elif item.title() not in menu_items.keys():
            continue

        #derermine the ordered item and add to total. If item not in dictionary then reprompt user
        total += menu_items[item.title()]

        #Display order total
        print(f"Total: ${total:.2f}")

    
main()
