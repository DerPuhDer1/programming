import automobile

#Create instances of automobile
auto1 = automobile.Automobile("Mercury", "Sable", "1234", 3.0, "Bob", 1998)
auto2 = automobile.Automobile("Honda", "Accord", "23456", 2.2, "Alice", 2003)

#Change auto2's year
auto2.__year = 2020

#Change auto1's owner
auto1.set_owner("Jerry")

auto_list = []
auto_list.append(auto1)
auto_list.append(auto2)

#Print each automobiles info
for auto in auto_list:
    auto.print_data()

print(f"Auto1 is {auto1.get_age()} years old")