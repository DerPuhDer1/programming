#Create a list
demo_list = [15, 8, 64, 25, 9, 11, 32, 41]

#Matrix dimensions 3 x 4
list_of_lists = [[2, 4, 7, 9],
                 [3, 7, 8, 4],
                 [1, 6, 5, 2]]


#Get data from lists
print(demo_list[2])

#Print the 8 in list_of_lists
print(list_of_lists[1] [2])

#Print all the values in my list_of_lists matrix
for number in demo_list:
    print(number)

print("\n")
#Iterate over the rows
for row in range(len(list_of_lists)):
    #Iterate over the column
    print(f"Row {row + 1} values")
    for column in range(len(list_of_lists[row])):
        print(list_of_lists[row][column])
