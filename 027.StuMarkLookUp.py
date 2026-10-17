# Given a dictionary of student names and marks, ask for a name and display their mark. If the name isn’t present, display Not found.
# Example: {"Asha": 85, "Ravi": 72}, lookup Ravi → 72

stu_list = {"Asha": 85, "Ravi": 72}

stu_name = input("Enter stu name:").capitalize()

print(stu_list.get(stu_name, "Not Found"))
