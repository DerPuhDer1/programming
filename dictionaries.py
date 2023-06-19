#Create a dictionary of names and scores
student_scores = {"Alice": 87, "Bob": 79, "Jerry": 94, "Sara": 90}

#Print Bob's score
print(student_scores["Bob"])

#print Sara's score
print(student_scores["Sara"])

#Declare a car dictionary
car = {"make": "Mercury", "model": "Sable", "year": 1998, "value": 10000, "engine": 3.0}

#get all the values from the student score dictionary
print("\n")
for student in student_scores:
    print(f"{student}: {student_scores[student]}")

#Get all the keys and values from the cars dictionary
print("\n")
for key, value in car.items():
    print(f"{key}: {value}")