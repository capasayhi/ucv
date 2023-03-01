import json

with open("studentsData.json", "r") as file:
    data = json.load(file)

format = {"first name": "", "last name": "", "age": "", "ID": ""}
print("Welcome professor.\n¿What do you want to do?")

action = input("Click on (c) to consult / (a) to add: ")

if action == "c":

    id = input("Enter student identity number to consult: ")

    for student in data["curso"]["students"]:
        if student["ID"] == id:
            print(student)

elif action == "a":
    format["first name"] = input("Enter the student first name: ")
    format["last name"] = input("Enter the student last name: ")
    format["age"] = input("Enter the student age: ")
    format["ID"] = input("Enter the student identity number:")

    data["curso"]["students"].append(format)

    with open("studentsData.json", "w+") as file:
        json.dump(data, file, indent=2)
else:
    print("Invalid entry verifies the character on enter")
