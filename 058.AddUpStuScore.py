# Given a dictionary of student names and scores, calculate and print the total of all the scores.
# Example: {"Asha": 80, "Ravi": 70, "Mina": 90} → 240

stu_list =  {"Asha": 80, "Ravi": 70, "Mina": 90}
total = 0

# for name,mark in stu_list.items():
#     total += mark
# print(total)


print(sum(stu_list.values()))
