#Reading files in python
#open the file
data_file = open("file.txt", "r")

#Create an empty dictionary
menu_item = {}

#Loop through data in file
for line_of_data in data_file:
    print(line_of_data)
    #Split line of data at the ", "
    keys_values = line_of_data.split(", ")
    #Create an entry to the dictionary. Remember to convert price to float
    menu_item[keys_values[0]] = float(keys_values[1])

#Close file
data_file.close()

for item, price in menu_item.items(): 
    print(f"{item}: ${price:.2f}")