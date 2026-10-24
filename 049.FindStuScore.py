# Use a dictionary of student names and scores. Ask for a name and print the score, or "Not found" if the name isn’t in the dictionary.
# Example: {"Asha": 85, "Ravi": 72}, lookup "Ravi" → 72

def LookUp(stu_list,stu_name):
    return stu_list.get(stu_name,"Not Found")


stu_list = {"Asha": 85, "Ravi": 72}
stu_name = input("Enter Student Name:").capitalize()

print(LookUp(stu_list, stu_name))
