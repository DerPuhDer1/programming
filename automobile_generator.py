import automobile

#Create an automobile
auto1 = automobile.Automobile("Mercury", "Sable", "1234", 3.0, "Bob")
auto2 = automobile.Automobile("Honda", "Accord", "23456", 2.2, "Alice")

auto_list = []
auto_list.append(auto1)
auto_list.append(auto2)

#Print each automobiles info
for auto in auto_list:
    print(auto.make)
    print(auto.model)
    print("\n")