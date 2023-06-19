#List demo
names = ["John", "Mary", "Alice", "Bob"]
demo_list = [10, 16, 24, 77, 2, 14, 9]

#Add values to the list
demo_list.append(5)
demo_list.append(63)
print(demo_list)

#Get number of items in list
number_of_items = len(demo_list)
print(f"number_of_items: {number_of_items}")

#Get values from the list

#Get first value from the list
print("\n")
print(demo_list[0])

#get the fourth value from the list
print(demo_list[3])

#get the tenth value from the list
#print(demo_list[9])

#print all items in the list
print("\n")
for item in demo_list:
    print(item)

print("\n")
for index in range(len(demo_list)):
    print(demo_list[index])

#print item at odd indexes
print("\n")
for index in range(1, number_of_items, 2):
    print(demo_list[index])

#print item at even indexes
print("\n")
for index in range(2, number_of_items, 2):
    print(demo_list[index])